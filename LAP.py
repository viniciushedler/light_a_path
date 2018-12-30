from imports import *

class LAP():
    '''O jogo em si'''

    def __init__(self):
        atribuir_psv(self, 'PSV_LAP')
        self.relogio = pygame.time.Clock()
        self.tela = Tela()
        self.lighty = Lighty()
        self.lista_objetos = [self.lighty]
        self.tela.grade()
    
    def main_loop(self):
        self.lighty.loop()
        self.tela.loop(self.lista_objetos)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return True
        return False
    
    def iniciar_jogo(self):
        sair = False
        while not sair:
            sair = self.main_loop()
            self.relogio.tick(self.RELOGIO_DELAY)

if __name__ == "__main__":
    lap = LAP()
    lap.iniciar_jogo()
    sair = False
    while not sair:
        sair = lap.main_loop()
