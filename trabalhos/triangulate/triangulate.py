# coding=UTF-8
import sys
import Geometria
from Geometria import *

#-----------------------------------------------#
# Lê dados do stdin como especificado
#-----------------------------------------------#
def get_data():
    num_pontos = int(raw_input())
    vertices = []
    for i in xrange(num_pontos):
        x, y = map(float, raw_input().split())
        # "gira" o poligono para que não tenha pontos em um mesmo y
        if i > 0:
            if y == vertices[i-1].y:
                y = y - 0.1
        vertices.append(Ponto(i+1,x,y))
    return vertices

def show_data(p):
    print len(p.faces)-1
    for i in xrange(1,len(p.faces)):
        print p.faces[i].inner.orig.id, p.faces[i].inner.prox.orig.id, p.faces[i].inner.ant.orig.id,p.faces[i].inner.prox.twin.face.id, p.faces[i].inner.ant.twin.face.id, p.faces[i].inner.twin.face.id

def main():
    # le da entrada
    vertices = get_data()

    # utiliza os vertices para formar um poligono
    poligono = Poligono(vertices)

    # xunxo para fazer funcionar
    # classifica os vertices e 
    #poligono.classify()

    # divide o poligono em subpoligonos monotônicos
    # O(n log n)
    sweep(poligono)

    # com o poligono dividido, realiza a triangulação
    # O(n) uma vez que triangulate executa no máximo
    # o número de triangulos que um poligono pode ter
    # sendo assim, n-2 vezes
    triangulate(poligono)

    # imprime o numero de triangulos que se formaram
    show_data(poligono)

    # encerra o programa
    return True

if __name__ == "__main__":
    sys.exit(main())
