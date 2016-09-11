import Geometria
from Geometria import *

#num_pontos = int(raw_input())
vertices = []
#for i in xrange(num_pontos):
#    x, y = map(int, raw_input().split())
#    vertices.append(Ponto(i+1,x,y))
vertices.append(Ponto(1, 9, 11))
vertices.append(Ponto(2, 7, 9))
vertices.append(Ponto(3, 7, 15))
vertices.append(Ponto(4, 6, 14))
vertices.append(Ponto(5, 5, 15))
vertices.append(Ponto(6, 3, 13))
vertices.append(Ponto(7, 5, 12))
vertices.append(Ponto(8, 4, 8))
vertices.append(Ponto(9, 2, 10))
vertices.append(Ponto(10, 1, 5))
vertices.append(Ponto(11, 3, 3))
vertices.append(Ponto(12, 5, 4))
vertices.append(Ponto(13, 7, 1))
vertices.append(Ponto(14, 7, 7))
vertices.append(Ponto(15, 8, 6))
p = Poligono(vertices)
#print p.segments
p.classify()
#print_v(p.vertices)

sweep(p)
triangulate(p)
#triangulate(p)
#for v in p.vertices:
#    handle_vertex(v)
#print_v(p.vertices)
#print_s(p.edges)
print '--------------------------------------'
print_f(p.faces)
#print p.faces
#p.monotone_decomposition()
