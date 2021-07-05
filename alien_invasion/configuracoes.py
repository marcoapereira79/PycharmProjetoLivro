"""Módulo de Configurações"""


class Configuracoes:
    """Uma classe para  armazenar todas as configurações da Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        self.tela_width = 1350
        self.tela_height = 700
        self.bg_color = (0, 0, 0)
        self.nave_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.frota_drop_speed = 10
        # frota-direcao igual a 1 representa a direita; -1 representa a esquerda
        self.frota_direcao = 1
        self.municao_width = 1
        self.municao_height = 15
        self.municao_color = 247, 20, 43
        self.municao_speed_factor = 1
        self.municoes_permitida = 3
