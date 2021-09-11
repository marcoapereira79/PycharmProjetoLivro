import pygame.font

class Registro_de_pontos():
    """Uma classe para mostrar informações sobre pontuação"""
    def __init__(self, ai_configuracoes, tela, stats):
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.ai_configuracoes = ai_configuracoes
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.text_color = (250, 250, 10)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial
        self.prep_pontos()

    def prep_pontos(self):
        """Transforma a pontuação na parte superior direita da tela"""
        # Transformo stat.pontos em string
        pontos_str = str(self.stats.pontos)
        # Passo a string para render que irá criar a imagem
        self.pontos_image = self.font.render(pontos_str, True, self.text_color, self.ai_configuracoes.bg_color)

        # Exibe a pontuação na parte superior direita da tela
        self.pontos_rect = self.pontos_image.get_rect()
        self.pontos_rect.right = self.tela_rect.right - 20
        self.pontos_rect.top = 20

    def show_pontos(self):
        """Desenha a pontuação na tela"""
        self.tela.blit(self.pontos_image, self.pontos_rect)


