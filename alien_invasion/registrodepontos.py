import pygame.font
from pygame.sprite import Group
from nave2 import Nave


class Registro_de_pontos():
    """Uma classe para mostrar informações sobre pontuação"""
    def __init__(self, ai_configuracoes, tela, estatistica):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.ai_configuracoes = ai_configuracoes
        self.estatistica = estatistica

        # Configurações de fonte para as informações de pontuação
        self.text_color = (250, 250, 10)
        self.text_color2 = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)
        self.font_2 = pygame.font.SysFont(None, 32)

        # Prepara a imagem da pontuação inicial
        self.prep_pontos()

        # Prepara a imagem da pontuação máxima alcançada
        self.prep_pontos_maxima()

        # Prepara a imagem do nível do jogardor no jogo
        self.prep_nivel()

        # Prepara a imagem da quantidade de naves disponiveis para o jogador batalhar no jogo
        self.prep_naves()

    def prep_pontos(self):
        """Transforma a pontuação na parte superior direita da tela"""
        # Transformo stat.pontos em string e fazemos a formatção dos pontos para separar 3 casas com vírgula
        pontos_arredondados = int(round(self.estatistica.pontos, -1))
        pontos_str = "{:,}".format(pontos_arredondados)
        # Passo a string para render que irá criar a imagem
        self.pontos_imagem = self.font.render(pontos_str, True, self.text_color, self.ai_configuracoes.bg_color)

        # Exibe a pontuação na parte superior direita da tela
        self.pontos_rect = self.pontos_imagem.get_rect()
        self.pontos_rect.right = self.tela_rect.right - 20
        self.pontos_rect.top = 20

    def prep_pontos_maxima(self):
        """Transforma a pontuação máxima em uma imagem renderizada"""
        pontos_maxima = round(self.estatistica.ler_pontuacao_maxima())
        pontos_maxima_str = "{:,}".format(pontos_maxima)
        self.pontos_maxima_imagem = self.font_2.render("recorde - " + pontos_maxima_str, True, self.text_color2, self.ai_configuracoes.bg_color)

        # Centraliza a pontuação máxima na parte superior da tela
        self.pontos_maxima_rect = self.pontos_maxima_imagem.get_rect()
        self.pontos_maxima_rect.centerx = self.tela_rect.centerx
        self.pontos_maxima_rect.top = self.tela_rect.top

    def prep_nivel(self):
        """Transforma o nivel em uma imagem renderizada"""
        self.nivel_image = self.font_2.render('level: ' + str(self.estatistica.nivel), True, self.text_color2, self.ai_configuracoes.bg_color)

        # Posiciona o nivel abaixo da pontuação
        self.nivel_rect = self.nivel_image.get_rect()
        self.nivel_rect.centerx = self.pontos_maxima_rect.right + 150
        self.nivel_rect.top = self.tela_rect.top

    def prep_naves(self):
        """Mostra quantas espaçonaves restam"""
        # Criação do grupo de Naves
        self.naves2 = Group()

        for nave_numero in range (self.estatistica.naves_abatidas):
            nave2 = Nave(self.ai_configuracoes, self.tela)
            nave2.rect.x = 10 + nave_numero * nave2.rect.width
            nave2.rect.y = 10
            self.naves2.add(nave2)


    def show_pontos(self):
        """Desenha a pontuação na tela"""
        self.tela.blit(self.pontos_imagem, self.pontos_rect)
        self.tela.blit(self.pontos_maxima_imagem, self.pontos_maxima_rect)
        self.tela.blit(self.nivel_image, self.nivel_rect)

        # Desenha as naves restantes do jogador
        self.naves2.draw(self.tela)


