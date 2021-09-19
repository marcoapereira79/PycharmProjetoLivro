import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""
    def __init__(self, ai_configuracoes, tela):
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__()
        self.tela = tela
        self.ai_configuracoes = ai_configuracoes
        # Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('/home/marco_user/Documentos/Projetos/Python_ProjetoLivro/imagens/aliens-1.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo á parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

        self.som_tela_fundo = pygame.mixer.Sound("/home/marco_user/Documentos/Projetos/Python_ProjetoLivro/audio/alien_fundo.ogg")

    def check_bordas(self):
        """Verifica se o alienígena chegou na borda da tela e devolve True"""
        tela_rect = self.tela.get_rect()
        if self.rect.right >= tela_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move o alienígena para a direita ou para a esquerda"""
        self.x += (self.ai_configuracoes.alien_speed_factor * self.ai_configuracoes.frota_direcao)
        self.rect.x = self.x

    def som_fundo(self):
        self.som_tela_fundo.play()
