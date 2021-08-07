class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena"""

    def __init__(self, ai_configuracoes):
        """Inicializa os dados estatísticos"""
        self.ai_configuracoes = ai_configuracoes
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.naves_abatidas = self.ai_configuracoes.nave_limit

