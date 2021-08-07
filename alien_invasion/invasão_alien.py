import pygame
from pygame.sprite import Group
from configuracoes import Configuracoes
from nave import Nave
from estat_game import GameStats
import jogo_funcoes as jf
from button import Button


def run_game():
    pygame.init()
    # objeto das Configurações do jogo
    ai_configuracoes = Configuracoes()
    # Tela do jogo
    tela = pygame.display.set_mode((ai_configuracoes.tela_width, ai_configuracoes.tela_height))
    # Nome da Tela
    pygame.display.set_caption("Space War")
    # Cria o botão Play
    play_button = Button(ai_configuracoes, tela, "Play")
    # Cria uma instância para armazenar dados estatíticos do jogo
    estatistica = GameStats(ai_configuracoes)
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
        jf.check_eventos(ai_configuracoes, tela, estatistica, play_button, nave, aliens, municoes)
        # Só xecutará se o game estiver ativo (game inativo se as vidas terminarem)
        if estatistica.game_active:
            nave.update_nave()
            jf.update_municoes(ai_configuracoes, tela, nave, aliens, municoes)
            jf.update_aliens(ai_configuracoes,estatistica, tela, nave, aliens, municoes)

        jf.update_tela(ai_configuracoes, estatistica ,tela, nave, aliens, municoes, play_button)



run_game()
