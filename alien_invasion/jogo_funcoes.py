import sys
import pygame
from municao import Municao
from alien import Alien


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


def check_eventos(ai_configuracoes, tela, nave, municoes):
    """Responde a eventos de pressionamento de teclas e do mouse"""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            check_keydown_events(evento, ai_configuracoes, tela, nave, municoes)
        elif evento.type == pygame.KEYUP:
            check_keyup_events(evento, nave)


def check_keyup_events(evento, nave):
    """Responde a solturas de tecla"""
    if evento.key == pygame.K_RIGHT:
        nave.move_direita = False
    elif evento.key == pygame.K_LEFT:
        nave.move_esquerda = False
    elif evento.key == pygame.K_q:
        sys.exit()


def update_tela(ai_configuracoes, tela, nave, aliens, municoes):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    tela.fill(ai_configuracoes.bg_color)
    # Redesenha todos os projéteis atrás da espçonave e dos alienígenas
    for municao in municoes.sprites():
        municao.desenha_projetil()
    nave.blitme()
    aliens.draw(tela)

    # Deixa a tela mais recente visível.
    pygame.display.flip()


def update_municoes(ai_configuracoes, tela, nave, aliens, municoes):
    """Atualiza as posicoes dos projéteis antigos, se o projétil chega ao fim da tela é removido"""
    # Atualiza a posição dos projéteis
    municoes.update()
    # Livra-se dos projéteis que desapareceram
    for municao in municoes.copy():
        if municao.rect.bottom <= 0:
            municoes.remove(municao)
    check_municao_alien_colisoes(ai_configuracoes, tela, nave, municoes, aliens)


def check_municao_alien_colisoes(ai_configuracoes, tela, nave, municoes, aliens):
    """Responde a colisões entre projéteis e alienígenas."""
    # Remove qualquer projétil e alienígena que tenham colidido
    colisoes = pygame.sprite.groupcollide(municoes, aliens, True, True)
    if len(aliens) == 0:
        # Destrói os projéteis existentes e cria uma nova frota
        municoes.empty()
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
    espaco_livre_y = (ai_configuracoes.tela_height - (3 *  alien_height) - nave_height)
    number_rows = int(espaco_livre_y / (2 * alien_height))
    return number_rows


def cria_frota(ai_configuracoes, tela, nave, aliens):
    """Cria uma frota completa de aliens"""
    # Cria um alienígena e calcula o nº de alienígenas numa linha
    alien = Alien(ai_configuracoes, tela)
    numero_aliens_x = get_number_aliens_x(ai_configuracoes, alien.rect.width)
    number_rows = get_number_rows(ai_configuracoes, nave.rect.height, alien.rect.height)
    # Cria a frota de alienígenas
    # laço para preencher as linhas da tela(eixo y) com aliens
    for row_number in range(number_rows):
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


def update_aliens(ai_configuracoes, aliens):
    """Verifica se a frota está numa das bordas e então atualiza as posições dos aliens"""
    check_frota_bordas(ai_configuracoes, aliens)
    aliens.update()
