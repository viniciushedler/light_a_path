from imports import *

def terminal(self=None):
    while True:
        try:
            exec(input(self.__str__() + ">>> "))
        except Exception as inst:
            print(type(inst))
            for arg in inst.args:
                print(arg)

def atribuir_psv(objeto, dic_nome):
    for index, value in globals()[dic_nome].items():
        setattr(objeto, index, value)

def calc_dist(p1, p2):
    p0 = [abs(p1[0]-p2[0]), abs(p1[1]-p2[1])]
    dist = hipotenusa(p0[0], p0[1])
    return dist

def hipotenusa(c1, c2):
    return (c1**2+c2**2)**.5


if __name__ == "__main__":
    pass