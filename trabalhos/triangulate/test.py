# coding=UTF-8
import Geometria
from Geometria import *

num_pontos = int(raw_input())
vertices = []
for i in xrange(num_pontos):
    x, y = map(float, raw_input().split())
    # "gira" o poligono para que não tenha pontos em um mesmo y
    if i > 0:
        if y == vertices[i-1].y:
            y = y - 0.1
    vertices.append(Ponto(i+1,x,y))
#vertices.append(Ponto(1, 1, 15))
#vertices.append(Ponto(2, 1, 5))
#vertices.append(Ponto(3, 5, 4))
#vertices.append(Ponto(4, 5, 16))
#vertices.append(Ponto(5, 3, 9.1))

#vertices.append(Ponto(1, 9, 11))
#vertices.append(Ponto(2, 7, 9))
#vertices.append(Ponto(3, 7, 15))
#vertices.append(Ponto(4, 6, 14))
#vertices.append(Ponto(5, 5, 15))
#vertices.append(Ponto(6, 3, 13))
#vertices.append(Ponto(7, 5, 12))
#vertices.append(Ponto(8, 4, 8))
#vertices.append(Ponto(9, 2, 10))
#vertices.append(Ponto(10, 1, 5))
#vertices.append(Ponto(11, 3, 3))
#vertices.append(Ponto(12, 5, 4))
#vertices.append(Ponto(13, 7, 1))
#vertices.append(Ponto(14, 7, 7))
#vertices.append(Ponto(15, 8, 6))
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
#print '--------------------------------------'
#print_f(p.faces)
#show_data(p)
print len(p.faces)-1
for i in xrange(1,len(p.faces)):
    print p.faces[i].inner.orig.id, p.faces[i].inner.prox.orig.id, p.faces[i].inner.ant.orig.id,p.faces[i].inner.prox.twin.face.id, p.faces[i].inner.ant.twin.face.id, p.faces[i].inner.twin.face.id

#print p.faces
#p.monotone_decomposition()
#for e in p.edges:
#    print e, e.face.id