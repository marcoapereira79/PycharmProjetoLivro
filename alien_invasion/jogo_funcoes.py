"""Módulo que armazena as  funções do jogo"""
import sys
import pygame
from municao import Municao
from alien import Alien



def check_keydown_events(evento, ai_configuracoes, tela, nave_espacial, municoes):
    """Responde a pressionamento de teclas"""
    if evento.key == pygame.K_RIGHT:
        nave_espacial.move_direita = True
    elif evento.key == pygame.K_LEFT:
        nave_espacial.move_esquerda = True
    elif evento.key == pygame.K_SPACE:                         #Esta condição cria um novo projétil e adiciona ao grupo de projéteis
        tiro_municao(ai_configuracoes, tela, nave_espacial, municoes)
    elif evento.key == pygame.K_q:
        sys.exit()

def check_eventos(ai_configuracoes, tela, nave_espacial, municoes):
    """Responde a eventos de pressionamento de teclas e do mouse"""
    for evento in pygame.event.get():                          #pegar cada evento
        if evento.type == pygame.QUIT:                         #caso seja solicitado a saída
            sys.exit()
        elif evento.type == pygame.KEYDOWN:                    #pressionamento de tecla
            check_keydown_events(evento, ai_configuracoes, tela, nave_espacial, municoes)
        elif evento.type == pygame.KEYUP:                      #soltura de tecla
            check_keyup_events(evento, nave_espacial)


def check_keyup_events(evento, nave_espacial):
    """Responde a solturas de tecla"""
    if evento.key == pygame.K_RIGHT:
        nave_espacial.move_direita = False
    elif evento.key == pygame.K_LEFT:
        nave_espacial.move_esquerda = False
    elif evento.key == pygame.K_q:
        sys.exit()


def update_tela(ai_configuracoes, tela, nave_espacial, aliens, municoes):
    """Atualiza as imagens na tela e alterna para a nova tela"""
    tela.fill(ai_configuracoes.bg_color)
    for municao in municoes.sprites():
        municao.desenha_projetil()
    nave_espacial.blitme()
    aliens.draw(tela)

    pygame.display.flip()


def update_municoes(municoes):
    """Atualiza as posicoes dos projéteis antigos, se o projétil chega ao fim da tela é removido"""
    municoes.update()
    for municao in municoes.copy():
        if municao.rect.bottom <= 0:                               #verifica se o projétil chegou ao fim da tela
            municoes.remove(municao)


def tiro_municao(ai_configuracoes, tela, nave_espacial, municoes):
    """Dispara um projétil se o limite ainda não foi lançado"""
    if len(municoes) < ai_configuracoes.municoes_permitida:         #Caso não tenha número máximo de munições na tela(3) , add munição
        nova_municao = Municao(ai_configuracoes, tela, nave_espacial)
        municoes.add(nova_municao)                                  #adicionando munição ao grupo municoes (criado no arquivo principal)



def criar_alien(ai_configuracoes, tela, aliens, qtde_aliens, linha):
    alien = Alien(ai_configuracoes, tela)                           #Cria uma nave alien
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * qtde_aliens
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * linha
    aliens.add(alien)


def get_numero_aliens_x(ai_configuracoes, alien_width):
    """Determina o número de alienígenas que cabem em uma linha"""
    espaco_livre_x = ai_configuracoes.tela_width - 2 * alien_width
    numero_aliens_x = int(espaco_livre_x / (2 * alien_width))
    return numero_aliens_x


def get_numero_linhas(ai_configuracoes, nave_height, alien_height):
    """Determina o número de linhas com alinígenas que cabem na tela"""
    espaco_livre_y = (ai_configuracoes.tela_height - (6 * alien_height) - nave_height)
    numero_linhas = int(espaco_livre_y / (2 * alien_height))
    return numero_linhas


def cria_frota(ai_configuracoes, tela, nave_espacial, aliens):
    """Cria uma frota completa de aliens"""
    alien = Alien(ai_configuracoes, tela)                                   #Cria um alienígena
    numero_aliens_x = get_numero_aliens_x(ai_configuracoes, alien.rect.x)   #Calcula a qtde de alienígenas que cabem numa linha
    numero_linhas = get_numero_linhas(ai_configuracoes, nave_espacial.rect.height, alien.rect.height)
    for linha in range(numero_linhas):                                      #laço para preencher as linhas da tela(eixo y) com aliens
        for qtde_aliens in range(numero_aliens_x):                          #laço para preencher uma linha (eixo x) com aliens
            criar_alien(ai_configuracoes, tela, aliens, qtde_aliens, linha)
        aliens.add(alien)                                                   #Adiciona o alienígena criado ao Group()

def update_aliens(aliens, ai_configuracoes):
    """Verifica se a frota está numa das bordas e então atualiza as posições dos aliens"""
    check_frota_bordas(ai_configuracoes, aliens)
    aliens.update()     #Usando o método update() no Grupo aliens , fará o método update() de cada alienígena ser chamado automaticamente


def check_frota_bordas(ai_configuracoes, aliens):
    """Responde se algum alien chegou na borda da tela"""
    for alien in aliens.sprites():
        if alien.check_bordas():
            trocar_direcao_frota(ai_configuracoes, aliens)
        break


def trocar_direcao_frota(ai_configuracoes, aliens):
    """Faz a frota inteira descer e mudar a direcao"""
    for alien in aliens.sprites():
        alien.rect.y += ai_configuracoes.frota_drop_speed                   #horda desce na tela
        ai_configuracoes.frota_direcao *= -1                                #muda a direção do alien






