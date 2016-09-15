# coding=UTF-8
import math
from math import sqrt
from math import acos, cos, degrees

class Ponto(object):
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "%s (%s,%s, %s)" % (self.id, self.x, self.y, self.z)
        
class Face(object):
    def __init__(self, id, inner):
        self.id = id
        self.inner = inner
    def __repr__(self):
        return "%s - edge: %s" % (self.id, self.inner)

class Edge(object):
    def __init__(self, id, v1, v2, face):
        self.id = id
        self.orig = v1
        self.face = face
        self.twin = None
        self.prox = None
        self.ant = None

        # não faz parte da DCEL
        self.v1 = v1
        self.v2 = v2
        self.helper = None

    def __repr__(self):
        return "%s {%s, %s}" % (self.id, self.v1.id, self.v2.id)

class Poliedro(object):
    def __init__(self, id, faces):
        self.id = id
        self.vertices = []
        self.faces = []

