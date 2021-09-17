import pygame
from pygame.sprite import Sprite


class Nave(Sprite):
    def __init__(self, ai_configuracoes, tela):
        """Inicializa a espaçonave e define sua posição inicial."""
        super(Nave, self).__init__()
        self.ai_configuracoes = ai_configuracoes
        self.tela = tela
        self.image = pygame.image.load('/home/marco_user/Documentos/Projetos/Python_ProjetoLivro/imagens/nave.bmp')
        self.rect = self.image.get_rect()
        self.tela_rect = tela.get_rect()
        self.rect.centerx = self.tela_rect.centerx  # Inicia cada nova espaçonave na parte inferior central da tela
        self.center = float(self.rect.centerx)   # Transforma self.rect.centerx em ponto flutuante
        self.rect.bottom = self.tela_rect.bottom  # Inicia cada nova espaçonave na parte inferior
