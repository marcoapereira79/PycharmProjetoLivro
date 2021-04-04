import pygame
from pygame.sprite import Sprite

class Municao(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave"""

    def __init__(self, ai_configuracoes, tela, nave_espacial):
        """Cria um objeto para o projétil na posição atual da espaçonave"""
        super(Municao, self).__init__()                                        #herdando de Sprite
        self.tela = tela
        self.rect = pygame.Rect(0, 0, ai_configuracoes.municao_width, ai_configuracoes.municao_height) #Cria um projétil em (0,0) e define a posição correta
        self.rect.centerx = nave_espacial.rect.centerx                                                 #rect do projétil igual ao da nave
        self.rect.top = nave_espacial.rect.top                                                         #rect top do projétil igual ao topo da nave
        self.y = float(self.rect.y)             #Armazena a posição do projétil como um valor decimal na orientação y para ajustes de velocidade do mesmo
        self.color = ai_configuracoes.municao_color
        self.speed_factor = ai_configuracoes.municao_speed_factor


    def update(self):
        """Move o projétil para cima na tela"""
        self.y -= self.speed_factor             #Dá velocidade ao projil alterando suaposição no eixo y (subindo na tela)
        self.rect.y = self.y                    #Atualiza a posição de rect


    def desenha_projetil(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.tela, self.color, self.rect)