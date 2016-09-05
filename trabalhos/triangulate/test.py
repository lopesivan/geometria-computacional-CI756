import Geometria
from Geometria import *

num_pontos = int(raw_input())
vertices = [] 
for i in xrange(num_pontos):
    x, y = map(int, raw_input().split())
    vertices.append(Ponto(i,x,y))

p = Poligono(vertices)

p.classify()
for v in p.vertices:
    classifica(v)
#print_v(p.vertices)
    
sweep(p)

#print_s(p.segments)

#p.monotone_decomposition()

#x = [1,1,2,3,4,5,5,5,6,6,7,8,9,9,9]
#print x
#while x:
#    v = []
#    v.append(x.pop())
#    print v
#    if x:
#        while x and x[-1] == v[0]:
#            print 'x[-1] ', x[-1], ' v ', v
#            v.append(x.pop())
#    print '---'