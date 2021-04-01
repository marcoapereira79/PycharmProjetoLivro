import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""

    def __init__(self, ai_configuracoes, tela):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alien, self).__init__()
        self.tela = tela
        self.ai_configuracoes = ai_configuracoes
        self.image = pygame.image.load('/home/marco_user/PycharmProjetoLivro/alien_invasion/imagens/aliens-3.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width       #Inicia cada novo alienígena próximo à parte superior esquerda tela
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)        #Armazena a posição exata do alienígena


    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        self.tela.blit(self.image, self.rect)




