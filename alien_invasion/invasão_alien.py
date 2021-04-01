import pygame                            # c ntêm a s funcionalidades para criar o jogo
from pygame.sprite import Group
from configuracoes import Configuracoes  # do módulo configurações importei a classe Configurações
from nave import Nave
import jogo_funcoes as jf               #importei o módulo jogo_funções.py com aliás jf



def run_game():
    pygame.init()                            # Inicializa o jogo e cria um objeto para a tela
    ai_configuracoes = Configuracoes()       #instanciei o objeto ai da Classe Configuracoes
    tela = pygame.display.set_mode((ai_configuracoes.tela_width, ai_configuracoes.tela_height)) #a tela é configurada chamando o objeto ai_...
    pygame.display.set_caption("Alien Invasion")
    nave_espacial = Nave(ai_configuracoes, tela)                #instanciei um objeto nave_espacial da classe Nave()
    municoes = Group()                       #Cria um grupo no qual serão armazenados as munições
    aliens = Group()                         #Cria um grupo vazio para armazenar os aliens do jogo
    jf.cria_frota(ai_configuracoes, tela, nave_espacial, aliens)   #Cria uma frota de aliens (usa configurações, tela e um grupo vazio de aliens)
    

    while True:   #Inicia o laço principal do jogo
        jf.check_eventos(ai_configuracoes, tela, nave_espacial, municoes) #checa eventos
        nave_espacial.update_nave()                #posicionamento da nave
        jf.update_municoes(municoes)               #verifica as municoes na tela se houve disparo
        jf.update_tela(ai_configuracoes, tela, nave_espacial, aliens,  municoes)   #update da tela



run_game()
