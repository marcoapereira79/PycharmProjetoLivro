"""Módulo de Configurações"""

class Configuracoes():
    """Uma classe para  armazenar todas as configurações da Invasão Alienígena"""
    def __init__(self):
        """Inicializa as configurações do jogo"""
        self.tela_width = 1359            #Configuração da tela , largura
        self.tela_height = 700             #Configuracao da tela , altura
        self.bg_color = (0, 0, 0)          #Configuração da cor de fundo da tela
        self.nave_speed_factor = 1.5       #Configurações da espaçonave para ajuste da velocidade
        self.alien_speed_factor = 1        #Configuração da espaçonave alienígena para ajuste de velocidade
        self.frota_drop_speed = 10         #Configuração da velocidade com que a frota desce na tela após chegar nas bordas da tela
        self.frota_direcao = 1          #fleet_direction -1 representa direção para a esquerda da tela, 1 seria para a direita
        self.municao_width = 1           #largura do projétil
        self.municao_height = 15           #tamanho do projétil
        self.municao_color = 247, 20, 43   #cor do projétil
        self.municao_speed_factor = 1      #velocidade do projétil
        self.municoes_permitida = 3        #atributo que limita a 3 tiros ao mesmo tempo na tela

