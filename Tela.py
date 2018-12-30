from imports import *


class Tela():
    '''Base para a tela'''

    def __init__(self):
        atribuir_psv(self, "PSV_TELA")
        self.surface = pygame.display.set_mode((self.TELA_LARGURA, self.TELA_ALTURA))
    
    def grade(self):
        for x in range(1,self.GRADE_QTD_X+1):
            pygame.draw.line(self.surface, (155,155,155), (x*self.TELA_LARGURA/self.GRADE_QTD_X,0), (x*self.TELA_LARGURA/self.GRADE_QTD_X, self.TELA_ALTURA))
        for y in range(1,self.GRADE_QTD_Y+1):
            pygame.draw.line(self.surface, (155,155,155), (0,y*self.TELA_ALTURA/self.GRADE_QTD_Y), (self.TELA_LARGURA, y*self.TELA_ALTURA/self.GRADE_QTD_Y))
    
    def blitar(self, objeto):
        self.surface.blit(objeto.sprite, (objeto.pos_x, objeto.pos_y))
    
    def loop(self, lista_objetos):
        self.surface.fill(self.COR_FUNDO)
        for objeto in lista_objetos:
            self.blitar(objeto)
        pygame.display.flip()

if __name__ == "__main__":
    pass
