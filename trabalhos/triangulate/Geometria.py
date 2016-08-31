# coding=UTF-8
import math
from math import sqrt
from math import acos, cos

class Vertice(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tipo = None
    def __str__(self):
        return "(%s,%s)" % (self.x,self.y)

class Segmento(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return "{%s, %s}"%(self.v1,self.v2)
    #-----------------------------------------------#
    # Calcula a intersecção de dois segmentos
    # Entrada: um segmento
    # Saida: ponto de interseccao,
    #        false caso nao exista
    #-----------------------------------------------#
    def intersection(self, seg):

        # caso o maior x de uma reta, seja menor que o menor x da outra
        max_x1 = max( self.v1.x, self.v2.x)
        min_x2 = min( seg.v1.x, seg.v2.x)
        if  max_x1 < min_x2:
            # falta tratar para quando o ponto dos segmentos sao os mesmos
            return False

        div1 = (self.v2.x - self.v1.x)
        div2 = (seg.v2.x - seg.v1.x)
        if ((div1 == 0) or (div2 == 0)):
            print "Error! Divisao por 0 nao permitida!"
            return False

        A1 = float((self.v2.y - self.v1.y) / div1)
        A2 = float((seg.v2.y - seg.v1.y) / div2)
        if A1 == A2:
            print "Segmentos paralelos"
            return False

        b1 = self.v2.y - A1 * self.v2.x
        b2 = seg.v2.y - A2 * seg.v2.x

        div = (A1 - A2)
        if div == 0:
            print "Error! Divisao por 0 nao permitida"
            return False

        x_intersec = float((b2 - b1) / div)

        # aqui soh aceita segmento no momento
        # adapatar para aceitar retas e semi-retas
        if (x_intersec < max(min(self.v1.x, self.v2.x),min(seg.v1.x, seg.v2.x)) or\
            x_intersec > min(max(self.v1.x, self.v2.x),max(seg.v1.x, seg.v2.x))):
            print x_intersec, "false"
            return False
        else:
            print "Se encontram em ", x_intersec
            return x_intersec

    # a fazer: retorna o vertice logo acima da aresta
    def helper_split(self):
        return True

    # a fazer: retorna o vertice logo abaixo da aresta
    def helper_merge(self):
        return True



class Triangulo(object):
    # no caso, recebe os indices dos vertices
    def __init__(self, vertices):
        self.vertices = []
        for v in vertices:
            self.vertices.append(v)

    def __str__(self):
        return "%s %s %s"%(self.vertices[0], self.vertices[1], self.vertices[2])




class Poligono(object):
    def __init__(self, vertices):
        self.num_triangulos = None
        self.triangulos = []
        self.segments = []
        self.vertices = vertices
    
        for i in xrange(len(vertices) - 1):
            self.segments.append(Segmento(vertices[i], vertices[i+1]))
        self.segments.append(Segmento(vertices[len(vertices)-1], vertices[0]))
        
    #-----------------------------------------------#
    # Decompoe o poligono em poligonos monotonicos
    # Entrada: poligono simples P 
    # Saida: uma divisao de P em poligono monotonico
    #-----------------------------------------------#
    def monotone_decomposition(self):
        print "monotone_decomposition()"
        print "..."
        Q = self.vertices[:]
        quick_order_y(Q, 0, len(Q)-1)
        print_v(Q) 
        classify(Q)
        print_v(Q)
        return True
    #-----------------------------------------------#
    # Calcula a triangulacao de um poligono
    # Entrada: self
    # Saida: um poligono triangulado,
    #        false caso nao exista
    #-----------------------------------------------#
    def triangulate(self):
        # orderna os vertices com relacao ao eixo x
        V = quick_order_x(self.vertices, 0, len(self.vertices)-1)

        # remove os dois primeiros vertices V
        return True
        
    #-----------------------------------------------#
    # Classifica os vertices em: start, split, merge,
    # regular ou end.
    # Entrada: uma lista de vertices
    # Saida: uma classificação dos vertices
    #-----------------------------------------------#    
    def classify(self):

        for i in xrange(0,len(self.vertices)):
            p1 = self.vertices[i]
            ref = self.vertices[i - 1]
            p2 = self.vertices[i - 2]

            x1, y1 = p1.x - ref.x, p1.y - ref.y
            x2, y2 = p2.x - ref.x, p2.y - ref.y
            print x1, x2 
            print "  ", ref, angle(p1.x, p1.y, p2.x, p2.y)

            if cross_sign(x1, y1, x2, y2):
                ref.tipo = "inner"
            else:
                ref.tipo = "outer"
            

        return True

#-----------------------------------------------#
# Ordenação de vértices pela coordenada y
# Entrada: uma lista de vertices
# Saida: a lista ordenada pela coordenada y
#-----------------------------------------------#    
def quick_order_y(v, esq, dir):
    pivo = esq
    for i in xrange(esq+1, dir+1):
        j = i 
        if v[j].y < v[pivo].y:
            aux = v[j]
            while j > pivo:
                v[j] = v[j-1]
                j -= 1
            v[j] = aux
            pivo += 1
    if pivo-1 >= esq:   
        quick_order_y(v, esq, pivo-1)
    if pivo+1 <= dir:
        quick_order_y(v, pivo+1, dir)


#-----------------------------------------------#
# Recebe dois vértices e retorna o angulo entre 
# angulo entre eles
# Entrada: 
# Saida: 
#-----------------------------------------------#    
def angle(x1, y1, x2, y2):
    dot = (x1 * x2) + (y1 * y2)
    denom = sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))
    return cos(dot/denom)

def cross_sign(x1, y1, x2, y2):
    return x1 * y2 > x2 * y1

def print_v(vertices):
    print "os vertices:"
    for v in vertices:
        print v, " ", v.tipo

def print_s(segments):
    print "os segmentos:"
    for s in segments:
        print s