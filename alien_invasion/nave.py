import pygame

class Nave():
    def __init__(self, ai_configuracoes, tela):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.ai_configuracoes = ai_configuracoes
        self.tela = tela
        self.image = pygame.image.load('/home/marco_user/Documentos/Projetos/Python_ProjetoLivro/imagens/nave_nova1.bmp')   #Carrega a imagem da espaçonave
        self.rect = self.image.get_rect()                    #atributo da superfície - o Pygame trata elementos como retângulos , rects
        self.tela_rect = tela.get_rect()
        self.rect.centerx = self.tela_rect.centerx            #Inicia cada nova espaçonave na parte inferior central da tela
        self.center = float(self.rect.centerx)                #Transforma self.rect.centerx em ponto flutuante para aceitar valores decimais
        self.rect.bottom = self.tela_rect.bottom              #Inicia cada nova espaçonave na parte inferior
        self.move_direita = False                             #Flag de movimento da nave para a direita
        self.move_esquerda = False                            #Flag de movimento da nave para a esquerda



    def update_nave(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento"""
        if self.move_direita and (self.rect.right < self.tela_rect.right):  #se flag True e se antes do FIM DIREITO da tela
            self.center += self.ai_configuracoes.nave_speed_factor          #utiliza o fator de 1.5 de movimento definido em Configurações

        if self.move_esquerda and self.rect.left > 0:                       #se a flag para a esquerda for True e não for o FIM ESQUERDO da tela
            self.center -= self.ai_configuracoes.nave_speed_factor          #utiliza o fator de 1.5 de movimento

        self.rect.centerx = self.center                                     #Atualiza o objeto rect(que controla a posição da nave) de acordo com self.center


    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.tela.blit(self.image, self.rect)