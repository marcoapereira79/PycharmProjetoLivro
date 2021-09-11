"""Módulo de Configurações"""


class Configuracoes:
    """Uma classe para  armazenar todas as configurações da Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        # Configuração da Tela
        self.tela_width = 1350
        self.tela_height = 700
        self.bg_color = (0, 0, 0)


        # Configurações da espaçonave
        self.nave_speed_factor = 1.5
        self.nave_limit = 3

        # Configurações dos aliens
        self.alien_speed_factor = 2
        self.frota_drop_speed = 5

        # frota-direcao igual a 1 representa a direita; -1 representa a esquerda
        self.frota_direcao = 1

        # Configuração da Munição
        self.municao_width = 2
        self.municao_height = 15
        self.municao_color = 247, 20, 43
        self.municao_speed_factor = 3
        self.municoes_permitida = 3

        # A taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa as configuracoes que mudam no decorrer do jogo"""
        self.nave_speed_factor = 1.5
        self.municao_speed_factor = 3
        self.alien_speed_factor = 2

        # frota_direcao igual a 1 representa a direita; -1 representa a esquerda
        self.frota_direcao = 1

        # Pontos por cada alien abatido
        self.alien_pontos = 50

    def increase_speed(self):
        """Aumenta as configuracoes de velocidade"""
        self.nave_speed_factor *= self.speedup_scale
        self.municao_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale