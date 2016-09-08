import Geometria
from Geometria import *

num_pontos = int(raw_input())
vertices = []
for i in xrange(num_pontos):
    x, y = map(int, raw_input().split())
    vertices.append(Ponto(i+1,x,y))

p = Poligono(vertices)
#print p.segments
p.classify()
#print_v(p.vertices)

sweep(p)
#for v in p.vertices:
#    handle_vertex(v)
print_v(p.vertices)
print_s(p.edges)
print_f(p.faces)
#p.monotone_decomposition()
