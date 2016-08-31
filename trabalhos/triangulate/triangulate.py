import sys
import Geometria
from Geometria import *

#-----------------------------------------------#
# Lê dados do stdin como especificado
#-----------------------------------------------#
def get_data():
    num_pontos = int(raw_input())
    for i in xrange(num_pontos):
        x, y = map(int, raw_input().split())
        vertices.append(Vertice(x,y))
    return vertices

def main():
    # le da entrada
    vertices = get_data()

    # utiliza os vertices para formar um poligono
    poligono = Poligono(vertices)

    # realiza a triangulacao
    poligono.triangulate()

    # imprime o numero de triangulos que se formaram
    print poligono.num_triangulos

    # em seguida, imprime os triangulos
    for i in xrange(poligono.num_triangulos):
        print poligono.triangulo[i]

    # encerra o programa
    return True

if __name__ == "__main__":
    sys.exit(main())
