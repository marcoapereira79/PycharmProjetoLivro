import pygame

class Nave:
    def __init__(self, ai_configuracoes, tela):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.ai_configuracoes = ai_configuracoes
        self.tela = tela
        self.imge = pygame.image.load('/home/marco_user/Documentos/Projetos/Python_ProjetoLivro/imagens/nave_nova1.bmp')
        self.rect = self.imge.get_rect()
        self.tela_rect = tela.get_rect()
        self.rect.centerx = self.tela_rect.centerx  # Inicia cada nova espaçonave na parte inferior central da tela
        self.center = float(self.rect.centerx)   # Transforma self.rect.centerx em ponto flutuante
        self.rect.bottom = self.tela_rect.bottom  # Inicia cada nova espaçonave na parte inferior
        self.move_direita = False                 # Flag de movimento da nave para a direita
        self.move_esquerda = False                # Flag de movimento da nave para a esquerda

    def update_nave(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        if self.move_direita and (self.rect.right < self.tela_rect.right):
            self.center += self.ai_configuracoes.nave_speed_factor

        if self.move_esquerda and self.rect.left > 0:
            self.center -= self.ai_configuracoes.nave_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.tela.blit(self.imge, self.rect)

    def centralizar_nave(self):
        """Centraliza a espaçonave na tela"""
        self.center = self.tela_rect.centerx