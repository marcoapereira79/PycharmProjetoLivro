import pygame
from pygame.sprite import Sprite


class Municao(Sprite):
    """Uma classe que administra projéteis disparados  pela espaçonave"""
    def __init__(self, ai_configuracoes, tela, nave, som_tiro):
        """Cria um objeto para o projétil na posição atual da espaçonave"""
        super().__init__()               # herdando de Sprite
        self.tela = tela
        self.rect = pygame.Rect(0, 0, ai_configuracoes.municao_width, ai_configuracoes.municao_height)
        # rect do projétil igual ao da nave
        self.rect.centerx = nave.rect.centerx
        # rect top do projétil igual ao topo da nave
        self.rect.top = nave.rect.top
        self.y = float(self.rect.y)
        self.color = ai_configuracoes.municao_color
        self.speed_factor = ai_configuracoes.municao_speed_factor
        self.som(som_tiro)

    def update(self):
        """Move o projétil para cima na tela"""
        # Dá velocidade ao projétil alterando sua posição no eixo y (subindo na tela)
        self.y -= self.speed_factor
        # Atualiza a posição de rect
        self.rect.y = self.y

    def desenha_projetil(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.tela, self.color, self.rect)

    def som(self, som_tiro):
        som_tiro.play()
