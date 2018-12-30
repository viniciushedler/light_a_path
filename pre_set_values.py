import pygame

PSV_TELA = {

    'TELA_ALTURA' : 400,
    'TELA_LARGURA' : 1400,
    'GRADE_QTD_X' : 10,
    'GRADE_QTD_Y' : 10,
    'COR_FUNDO' : (0,0,0)
}

PSV_LIGHTY = {
    'aceleracao' : 1,
    'velocidade_max' : 5,
    'velocidade_x' : 0,
    'velocidade_y': 0,
    'velocidade_total' : 0,
    'pos_x' : PSV_TELA['TELA_LARGURA']/2,
    'pos_y' : PSV_TELA['TELA_ALTURA']/2,
    'LARGURA' : 20,
    'ALTURA' : 20,
}
PSV_LIGHTY['pos'] = PSV_LIGHTY['pos_x'], PSV_LIGHTY['pos_y']
PSV_LIGHTY['sprite'] = pygame.Surface((PSV_LIGHTY['LARGURA'],PSV_LIGHTY['ALTURA']))
PSV_LIGHTY['sprite'].fill((155,155,155))

PSV_LAP = {
    'RELOGIO_DELAY' : 20
}