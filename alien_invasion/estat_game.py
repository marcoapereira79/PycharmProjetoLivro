
class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena"""

    def __init__(self, ai_configuracoes, pontos = 0):
        """Inicializa os dados estatísticos"""
        self.ai_configuracoes = ai_configuracoes
        self.reset_stats()
        self.game_active = False
        self.pontuacao_maxima()

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.naves_abatidas = self.ai_configuracoes.nave_limit
        # Para reiniciar a pontuação sempre que um novo jogo começar
        self.pontos = 0
        self.nivel = 1


    def pontuacao_maxima(self):
        """Escreve o recorde de pontos no arquivo recorde para registro"""
        recorde = 'recorde.txt'
        y = str(self.pontos)
        if self.verifica_arquivo() and self.pontos > 0:
            with open(recorde, 'w+') as file_object:
                file_object.write(y)

        if not self.verifica_arquivo():
            with open(recorde, 'w+') as file_object:
                file_object.write(y)


    def ler_pontuacao_maxima(self):
        """Faz a leitura do arquivo recorde"""
        recorde = 'recorde.txt'
        with open(recorde, 'r') as file_object:
            linhas = file_object.readlines()

        for linha in linhas:
            n_int = linha

        return int(n_int)

    def verifica_arquivo(self):
        """Testa de o arquivo recorde realmente existe"""
        recorde = 'recorde.txt'
        try:
            a = open(recorde, 'r')
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True

        recorde.close()
