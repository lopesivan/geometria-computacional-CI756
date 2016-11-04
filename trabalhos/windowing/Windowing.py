# coding=UTF-8
import math
from math import sqrt
from math import acos, cos, degrees

class Ponto(object):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.edge = None

        self.tipo = None
        self.theta = None

    def __repr__(self):
        return "%s (%s,%s)" % (self.id, self.x, self.y)

class Edge(object):
    def __init__(self, id, v1, v2, face):
        self.id = id
        self.orig = v1
        self.face = face
        self.twin = None
        self.prox = None
        self.ant = None


    def __repr__(self):
        return "%s {%s, %s}" % (self.id, self.v1.id, self.v2.id)

class Window(object):
    def __init__(self, id, x1, x2, y1, y2):
        self.id = id
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __repr__(self):
        return '%s [%s:%s]x[%s:%s]' % (self.id, self.x1, self.x2, self.y1, self.y2)

        
#-----------------------------------------------#
# Funções helper
#-----------------------------------------------#
def distancia(e, v):
    num = (e.v2.y - e.v1.y)*v.x - (e.v2.x - e.v1.x)*v.y + e.v2.x * e.v1.y - e.v2.y * e.v1.x
    denom = sqrt( (e.v2.y - e.v1.y)**2 + (e.v2.x - e.v1.x)**2 )
    if denom == 0:
        print "divisao por 0"
        return False
    else:
        return  num / denom

# o vertice 'q' está abaixo de 'p' caso a coord. y seja menor
# ou se a coord. y for igual, usa a coord. x mais à direita
def abaixo(p, q):
    if (q.y < p.y or (q.y == p.y and q.x < p.x) ):
        return True
    return False


# o vertice 'q' está acima de 'p' caso a coord. y seja maior
# ou se a coord. y for igual, usa a coord. x mais à direita
def acima(p, q):
    if (q.y > p.y) or (q.y == p.y and q.x > p.x):
        return True
    return False

def cross_sign(x1, y1, x2, y2):
    return x1 * y2 < x2 * y1
