# coding=UTF-8
import windowing
from windowing import *

class Point(object):
    def __init__(self, x, y, segment=None):
        self.x = x
        self.y = y
        self.segment = segment

    def __repr__(self):
        return "(%s,%s) - %s" % (self.x, self.y, self.segment.id)

def getKey(point):
    return point.x

class Segment(object):
    def __init__(self, id, x1, x2, y1, y2):
        self.id = id
        if y1 > y2:
            self.upper = Point(x1, y1, self)
            self.lower = Point(x2, y2, self)
            if x1 < x2:
                self.side = True
            else:
                self.side = False
        else:
            self.upper = Point(x2, y2, self)
            self.lower = Point(x1, y1, self)
            if x2 < x1:
                self.side = True
            else:
                self.side = False
        self.reported = False

    def __repr__(self):
        return "%s" % (self.id)

class Window(object):
    def __init__(self, x, x1, y, y1):
        self.x1 = x1
        self.y1 = y1
        self.x = x
        self.y = y

class Node(object):
    def __init__(self, key, point):
        self.key = key
        self.point = point
        self.left = None
        self.right = None
        self.tree_assoc = None
        self.height = 1

    def __repr__(self):
        return "%s (%s,%s) %s" % (self.key, self.point.x, self.point.y, self.height)

class IntNode(object):
    def __init__(self, interval):
        self.key = interval
        self.segments = None
        self.left = None
        self.right = None
        self.height = 1

    def __repr__(self):
        return "%s %s - S:%s" % (self.key, self.height, self.segments)

class Interval(object):
    def __init__(self, x, x1, closed, semi=False):
        if x < x1:
            self.left = x 
            self.right = x1
        else:
            self.left = x1
            self.right = x
        self.semiclosed = semi
        self.closed = closed

    def __repr__(self):
        if self.semiclosed == 1:
            return "(%s:%s]" % (self.left, self.right)
        if self.semiclosed == 2:
            return "[%s:%s)" % (self.left, self.right)
        if self.closed:
            return "[%s:%s]" % (self.left, self.right)
        else:
            return "(%s:%s)" % (self.left, self.right)

#---------------------------------------------------#
# Entrada: uma coleção de pontos, e um booleano
#          indicando por qual coordenada será 
#          usada como chave (true para eixo x)
# Saída: uma arvore binária balanceada
#---------------------------------------------------#
class ArvBinBusca(object):
    def __init__(self, P, x_coord=True):
        self.root = None
        if x_coord:
            for point in P:
                self.root = insert_x( self.root, point )
        else:
            for point in P:
                self.root = insert_y( self.root, point )

    def __repr__(self):
        return "%s (%s,%s) %s" % (self.root.key, self.root.point.x, self.root.point.y, self.root.height)