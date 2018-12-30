# light_a_path
# V 0.2
Primeiro passo dado

RELATÓRIO:
.
.
.
    pre_set_values:
        ---Arquivo que contém os valores definidos antes do programa ser inciado
        ...e que podem ser mudados pelo programador---
        VALORES:
            [X] PSV_TELA:
                [X] TELA_ALTURA
                [X] TELA_LARGURA
                [X] GRADE_QTD_X
                [X] GRADE_QTD_Y
                [X] COR_FUNDO
            [X] PSV_LIGHTY:
                [X] aceleracao
                [X] velocidade_max
                [X] velocidade_x
                [X] velocidade_y
                [X] velocidade_total
                [X] pos_x
                [X] pos_y
                [X] pos
                [X] sprite
.
.
.
    imports:
        ---Arquivo que cuida dos imports---
.
.
.
    funcoes:
        ---Arquivo que contém funções que não estão presas a nenhum objeto---
        FUNÇÕES:
.
            [x] terminal():
                [X] Executa loop que replica o terminal dentro do programa;
.
            [X] atribuir_psv(objeto, dic_nome):
                [X] Atribui os valores do dicionário do arquivo pre_set_values
                ...(que contém o mesmo nome recebido como parâmetro) ao objeto;
.
            [X] hipotenusa(c1, c2):
                [X] Calcula e retorna a hipotenusa pelo cateo 1 e cateto 2 (que
                ...representam um par ordenado);
                
.
            [X] calc_dist(p1, p2):
                [X] calcula a difereça entre o x e o y de dois pontos;
                [X] retorna a hipotenusa desses dois valores;
                [X] usa a função definida hipotenusa;
.
.
.
    Tela:
        ---Objeto que cuidará do output---   
        ATRIBUTOS:
            [X] TELA_ALTURA
            [X] TELA_LARGURA
            [X] GRADE_QTD_X
            [X] GRADE_QTD_Y
            [X] COR_FUNDO
            [X] surface
.
        MÉTODOS:
.
            [X] __init__(self):
                [X] Atribuí os dados do PSV_TELA ao objeto;
                [X] Cria uma tela;
.
            [X] grade(self):
                [X] Cria uma grade;
                [X] Usa os valores inseridos em PSV_TELA,
                ... (GRADE_QTD_X, GRADE_QTD_Y);
.
            [X] blitar(self, objeto):
                [X] Na sua surface, blita a sprite do objeto passado como parâmetro;
.
            [X] loop(self, lista_objetos):
                [X] Preenche a tela com a cor de fundo;
                [X] Com a função blitar, blita cada um dos objetos na lista passada
                ...como parâmetro;
                [X] Atualiza a tela (pygame.display.flip())
                [ ] Checa quais objetos não tiveram atualizações visuais;
                [ ] Não atualiza objetos que se mantiveram visivelmente iguais;
.
.
.
    Lighty:
        ---Personagem jogável---
        ATRIBUTOS:
            [X] aceleracao
            [X] velocidade_max
            [X] velocidade_x
            [X] velocidade_y
            [X] velocidade_total
            [X] pos_x
            [X] pos_y
            [X] pos
            [X] sprite
.
        MÉTODOS:
.
            [X] tratar_velocidade(self):
                [X] Aumenta a velocidade de lighty nas direções que o usuário mandar;
                [X] Sempre desacelera lighty um pouco;
                [X] Limita a velocidade total à um máximo (lighty não pode ser mover
                ...em uma velocidade N vertical e N horizontal se a velocidade máxima
                ...é N)
                [X] Atualiza a velocidade total de lighty;
.
            [X] tratar_posicao(self):
                [X] Atualiza a posição de lighty;
                [ ] Trata colisão;
.
            [X] loop(self):
                [X] executa tratar_velocidade();
                [X] executa tratar_posicao();
.
.
.
.
    LAP:
        ---Objeto que reunirá todos os outros, executando o jogo---
        ATRIBUTOS:
            [X] tela
            [X] lighty
            [X] lista_objetos
            [X] relogio
.
        MÉTODOS:
            [X] __init__(self):
                [X] Cria e atribuí um objeto Tela;
.
            [X] main_loop(self):
                [X] Roda o loop do objeto lighty;
                [X] Roda o loop do objeto tela;
                [X] Retorna se o usuário clicou para fechar o jogo (boolean);
                [ ] Roda o loop dos inimigos;
.
            [X] iniciar_jogo(self):
                [X] Inicia o jogo;
                [X] Roda o main loop;
                [X] Fecha o jogo se o main loop retornar True;
                [X] Espera o delay do relogio;




LISTA DO QUE É NECESSÁRIO:
[X] Criar classe jogável (Lighty)
[ ] Fazer a classe Lighty pular em vez de se movimentar na vertical
[ ] Criar classe Inimigo
[ ] Criar colisão
[ ] Criar ferramente para construção de mapas
[X] Fazer a classe Tela tratar o personagem jogável
[ ] Fazer a classe Tela tratar os inimigos

LISTA DO QUE É DESEJÁVEL:
[ ] Criar decoração
[ ] Fazer a classe Tela não atualizar áreas que permanecem iguais