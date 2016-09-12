#!/usr/bin/python
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
                y = y + 0.1
        vertices.append(Ponto(i+1,x,y))
    return vertices

def show_data(p):
    print len(p.vertices)
    for v in p.vertices:
        print int(v.x), int(v.y)
    print len(p.faces)-1
    for i in xrange(1,len(p.faces)):
        print p.faces[i].inner.orig.id, p.faces[i].inner.prox.orig.id, p.faces[i].inner.ant.orig.id,p.faces[i].inner.prox.twin.face.id, p.faces[i].inner.ant.twin.face.id, p.faces[i].inner.twin.face.id

def main():
    # le da entrada
    vertices = get_data()
    if len(vertices) < 3:
        print 'ao menos 3 vertices são necessários'
        return False
    # utiliza os vertices para formar um poligono
    # O(n), uma vez que executa 2n operações
    poligono = Poligono(vertices)



    #------------------------------------------------
    # monotone_decomposition():
    #   tempo para dividir o poligono em sub-poligonos
    #   monotônicos é O(n log n).
    monotone_decomposition(poligono)

    #------------------------------------------------
    # triangulate(): 
    #   tempo para dividir os sub-poligonos monotônicos 
    #   é O(n).
    # onde n é o número de vértices
    triangulate(poligono)

    # imprime como especificado
    show_data(poligono)

    return True

if __name__ == "__main__":
    sys.exit(main())
