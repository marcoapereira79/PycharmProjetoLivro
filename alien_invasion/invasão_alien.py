import pygame
from pygame.sprite import Group
from configuracoes import Configuracoes
from nave import Nave
import jogo_funcoes as jf


def run_game():
    pygame.init()
    ai_configuracoes = Configuracoes()
    tela = pygame.display.set_mode((ai_configuracoes.tela_width, ai_configuracoes.tela_height))
    pygame.display.set_caption("Space War")
    # Cria uma espaçonave
    nave = Nave(ai_configuracoes, tela)
    # Cria um grupo no qual armazeno os projéteis
    municoes = Group()
    # Cria um grupo no qual armazeno os aliens
    aliens = Group()
    # Cria a frota de alienígenas
    jf.cria_frota(ai_configuracoes, tela, nave, aliens)

    #Inicia o laço principal do jogo
    while True:
        jf.check_eventos(ai_configuracoes, tela, nave, municoes)
        nave.update_nave()
        jf.update_municoes(ai_configuracoes, tela, nave, aliens, municoes)
        jf.update_aliens(ai_configuracoes, aliens)
        jf.update_tela(ai_configuracoes, tela, nave, aliens, municoes)


run_game()
