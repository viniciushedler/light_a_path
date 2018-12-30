from imports import *

class Lighty():
    '''Personagem jogável'''

    def __init__(self):
        atribuir_psv(self, "PSV_LIGHTY")
    
    def tratar_velocidade(self):
        if self.velocidade_x>0:
            self.velocidade_x -= self.aceleracao/2
        elif self.velocidade_x<0:
            self.velocidade_x += self.aceleracao/2
        if self.velocidade_y>0:
            self.velocidade_y -= self.aceleracao/2
        elif self.velocidade_y<0:
            self.velocidade_y += self.aceleracao/2

        right = False
        left = False
        up = False
        down = False
        # print(pygame.key.get_pressed())
        for index in range(len(pygame.key.get_pressed())):
            if pygame.key.get_pressed()[index]:
                print(index)
                if index==0:
                    a = 1/0
                if index == 273:
                    up = True
                elif index == 274:
                    down = True
                elif index == 275:
                    right = True
                elif index == 276:
                    left = True
            
        if right and not self.velocidade_total >= self.velocidade_max:
            self.velocidade_x += self.aceleracao
        if left and not self.velocidade_total >= self.velocidade_max:
            self.velocidade_x -= self.aceleracao
        if down and not self.velocidade_total >= self.velocidade_max:
            self.velocidade_y += self.aceleracao
        if up and not self.velocidade_total >= self.velocidade_max:
            self.velocidade_y -= self.aceleracao
        
        self.velocidade_total = hipotenusa(self.velocidade_x, self.velocidade_y)
    
    def tratar_posicao(self):
        self.pos_x += int(self.velocidade_x)
        self.pos_y += int(self.velocidade_y)
    
    def loop(self):
        self.tratar_velocidade()
        self.tratar_posicao()


    