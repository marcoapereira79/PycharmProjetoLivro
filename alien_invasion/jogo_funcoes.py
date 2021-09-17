import sys
import pygame
from municao import Municao
from alien import Alien
from time import sleep


def check_keydown_events(evento, ai_configuracoes, tela, nave, municoes):
    """Responde a pressionamento de teclas"""
    if evento.key == pygame.K_RIGHT:
        nave.move_direita = True
    elif evento.key == pygame.K_LEFT:
        nave.move_esquerda = True
    elif evento.key == pygame.K_SPACE:
        # Cria um novo projétil e o adiciona ao grupo de projéteis
        tiro_municao(ai_configuracoes, tela, nave, municoes)
    elif evento.key == pygame.K_q:
        sys.exit()


def check_eventos(ai_configuracoes, tela, estatistica, rp,play_button, nave, aliens, municoes):
    """Responde a eventos de pressionamento de teclas e do mouse"""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            check_keydown_events(evento, ai_configuracoes, tela, nave, municoes)
        elif evento.type == pygame.KEYUP:
            check_keyup_events(evento, nave)
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_configuracoes, tela, estatistica, rp, play_button, nave, aliens, municoes, mouse_x, mouse_y)

def check_play_button (ai_configuracoes, tela, estatistica, rp, play_button, nave, aliens, municoes, mouse_x, mouse_y):
    """Inicia um novo jogo quando o jogador clicar em Play e se o jogo não estiver ativo"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not estatistica.game_active:
        # Reinicia as configurações do jogo
        ai_configuracoes.initialize_dynamic_settings()
        # Oculta o cursor do mouse
        pygame.mouse.set_visible(False)

        # Reinicia os dados estatísticos do jogo
        estatistica.reset_stats()

        # Torna o jogo ativo se o botão Play for clicado
        estatistica.game_active = True

        # Reinicia as imagens do painel de pontuação
        rp.prep_pontos()
        rp.prep_pontos_maxima()
        rp.prep_nivel()
        rp.prep_naves()

        # Esvazia a lista de aliens e de projéteis
        aliens.empty()
        municoes.empty()

        # Cria uma nova frota e centraliza a nave
        cria_frota(ai_configuracoes, tela, nave, aliens)
        nave.centralizar_nave()


def check_keyup_events(evento, nave):
    """Responde a solturas de tecla"""
    if evento.key == pygame.K_RIGHT:
        nave.move_direita = False
    elif evento.key == pygame.K_LEFT:
        nave.move_esquerda = False
    elif evento.key == pygame.K_q:
        sys.exit()


def update_tela(ai_configuracoes, estatistica,rp ,tela, nave, aliens, municoes, play_button):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    tela.fill(ai_configuracoes.bg_color)

    # Redesenha todos os projéteis atrás da espçonave e dos alienígenas
    for municao in municoes.sprites():
        municao.desenha_projetil()
    # Desenha a nave chamando a função da Classe Nave
    nave.blitme()

    # desenha o Grupo sprite
    aliens.draw(tela)

    # Desenha a informação sobre pontuação
    rp.show_pontos()

    # Desenha o botão Play se o jogo estiver inativo
    if not estatistica.game_active:
        play_button.draw_button()

    # Deixa a tela mais recente visível.
    pygame.display.flip()


def update_municoes(ai_configuracoes, tela, nave, municoes, aliens, estatistica, rp):
    """Atualiza as posicoes dos projéteis antigos, se o projétil chega ao fim da tela é removido"""
    # Atualiza a posição dos projéteis
    municoes.update()
    # Livra-se dos projéteis que desapareceram
    for municao in municoes.copy():
        # Se a munição chegar ao fim da tela
        if municao.rect.bottom <= 0:
            municoes.remove(municao)
    check_municao_alien_colisoes(ai_configuracoes, tela, nave, municoes, aliens, estatistica, rp)


def check_municao_alien_colisoes(ai_configuracoes, tela, nave, municoes, aliens, estatistica, rp):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham colidido, colisões recebe uma lista
    colisoes = pygame.sprite.groupcollide(municoes, aliens, True, True)
    # No caso de colisões
    if colisoes:
        # Para verificar na lista colisões , os aliens que colidiram com o tiro
        for aliens in colisoes.values():
            estatistica.pontos += ai_configuracoes.alien_pontos * len(aliens)
            # mostra o painel de pontos com a atualização dos pontos
            rp.prep_pontos()
        checa_pontuacao_maxima(estatistica, rp)

    # Se todos os aliens forem abatidos
    if len(aliens) == 0:
        # Destrói os projéteis existentes , aumenta a velocidade do jogo
        municoes.empty()
        ai_configuracoes.increase_speed()

        # Aumenta o nivel do jogador
        estatistica.nivel += 1
        rp.prep_nivel()

        # Cria uma nova frota
        cria_frota(ai_configuracoes, tela, nave, aliens)


def tiro_municao(ai_configuracoes, tela, nave, municoes):
    """Dispara um projétil se o limite ainda não foi lançado"""
    # Cria um novo projétil e o adiciona ao grupo de projéteis
    if len(municoes) < ai_configuracoes.municoes_permitida:
        nova_municao = Municao(ai_configuracoes, tela, nave)
        municoes.add(nova_municao)


def create_alien(ai_configuracoes, tela, aliens, alien_number, row_number):
    # Cria uma nave alien e o posiciona na linha
    alien = Alien(ai_configuracoes, tela)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(ai_configuracoes, alien_width):
    """Determina o número de alienígenas que cabem em uma linha"""
    espaco_livre_x = ai_configuracoes.tela_width - (2 * alien_width)
    numero_aliens_x = int(espaco_livre_x / (2 * alien_width))
    return numero_aliens_x


def get_number_rows(ai_configuracoes, nave_height, alien_height):
    """Determina o número de linhas com alinígenas que cabem na tela"""
    espaco_livre_y = ((ai_configuracoes.tela_height ) - (3 *  alien_height) - nave_height)
    number_rows = int(espaco_livre_y / (2 * alien_height))
    return number_rows


def cria_frota(ai_configuracoes, tela, nave, aliens):
    """Cria uma frota completa de aliens"""
    # Cria um alienígena e calcula o nº de alienígenas numa linha
    alien = Alien(ai_configuracoes, tela)
    numero_aliens_x = get_number_aliens_x(ai_configuracoes, alien.rect.width)
    number_rows = int(get_number_rows(ai_configuracoes, nave.rect.height, alien.rect.height))
    # Cria a frota de alienígenas
    # laço para preencher as linhas da tela(eixo y) com aliens
    for row_number in range(number_rows ):
        # laço para preencher uma linha (eixo x) com aliens
        for alien_number in range(numero_aliens_x):
            create_alien(ai_configuracoes, tela, aliens, alien_number, row_number)
            # Adiciona o alienígena criado ao Group()
        aliens.add(alien)


def check_frota_bordas(ai_configuracoes, aliens):
    """Responde se algum alien chegou na borda da tela"""
    for alien in aliens.sprites():
        if alien.check_bordas():
            trocar_direcao_frota(ai_configuracoes, aliens)
            break


def trocar_direcao_frota(ai_configuracoes, aliens):
    """Faz a frota inteira descer e mudar a direcao"""
    for alien in aliens.sprites():
        # horda desce na tela
        alien.rect.y += ai_configuracoes.frota_drop_speed
    # muda a direção do alien
    ai_configuracoes.frota_direcao *= -1


def update_aliens( ai_configuracoes,estatistica, tela, rp, nave, aliens, municoes  ):
    """Verifica se a frota está numa das bordas e então atualiza as posições dos aliens"""
    # Checa se a horda chegou nas bordas
    check_frota_bordas(ai_configuracoes, aliens)

    # Atualiza o movimento do alien
    aliens.update()

    # Verifica se houve colisões entre alienígenas e a espaçonave
    if pygame.sprite.spritecollideany(nave, aliens):
        nave_abatida(ai_configuracoes, estatistica, tela, rp, nave, aliens, municoes)

     # Verifica se há algum alienígena que atingiu o fundo da tela sem ser destruído
    checa_aliens_fundo(ai_configuracoes, estatistica, tela, rp, nave, aliens, municoes)


def nave_abatida(ai_configuracoes, estatistica, tela, rp, nave, aliens, municoes):
    """Responde ao fato de a espaçonave ter sido atingida por um alienigena"""
    # Se houverem naves (vida)
    if estatistica.naves_abatidas > 0:
        # Decrementa naves abatidas
        estatistica.naves_abatidas -= 1
        # Faz uma pausa
        sleep(0.5)
        # Atualiza o painel de pontuações
        rp.prep_naves()
    else:
        estatistica.game_active = False
        pygame.mouse.set_visible(True)

    # Esvazia a lista de alienígenas e de projéteis
    aliens.empty()
    municoes.empty()

    # Cria uma nova frota e centraliza a espaçonave
    cria_frota(ai_configuracoes, tela, nave, aliens)
    nave.centralizar_nave()


def checa_aliens_fundo(ai_configuracoes, estatistica, tela, rp, nave, aliens, municoes):
    """Verifica se algum alienigena alcançou a parte inferior da tela"""
    tela_rect = tela.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= tela_rect.bottom:
            # Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            nave_abatida(ai_configuracoes, estatistica, tela, rp, nave, aliens, municoes)
            break

def checa_pontuacao_maxima(estatistica, rp):
    """Verifica se há uma nova pontuação máxima"""
    x = estatistica.ler_pontuacao_maxima()
    if estatistica.pontos > x:
        estatistica.pontuacao_maxima ()
        p = estatistica.ler_pontuacao_maxima()
        rp.prep_pontos_maxima()


