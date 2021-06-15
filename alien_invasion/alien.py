import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""
    def __init__(self, ai_configuracoes, tela):
        """Inicializa o alienígena e define sua posição inicial."""
        super(Alien, self).__init__()
        self.tela = tela
        self.ai_configuracoes = ai_configuracoes
        self.image = pygame.image.load('/home/marco_user/Documentos/Projetos/Python_ProjetoLivro/imagens/aliens-1.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width    #Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)                 #Armazena a posição exata do alienígena


    def check_bordas(self):
        """Verifica se o alienígena chegou na borda da tela e devolve True"""
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right:        #SE frota alien na borda direita da tela
            return True
        elif self.rect.left <= 0:                             #SE frota alien na borda esquerda da tela
            return True


    def update(self):
        """Move o alienígena para a direita ou para a esquerda"""
        self.x += (self.ai_configuracoes.alien_speed_factor * self.ai_configuracoes.frota_direcao) #Soma o fator de velocidade ao eixo x da imagem do alien
        self.rect.x = self.x #Atualizo a posição do rect do alien




