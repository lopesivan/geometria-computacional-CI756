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
        return "%s (%s,%s,%s)" % (self.id, self.x, self.y, self.z)
    #def __eq__(self, other):
    #    if self.x == other.x and self.y == other.y and self.z == other.z:
    #        return True
    #    else:
    #        return False

class Face(object):
    def __init__(self, id, inner, vertices):
        self.id = id
        self.inner = inner
        self.vertices = vertices
    def __repr__(self):
        return "%s - edge: %s" % (self.id, self.inner)

class Edge(object):
    def __init__(self, id, v1, v2, face):
        self.id = id
        self.orig = v1
        self.face = face
        self.twin = None
        self.next = None
        self.prev = None
        self.v1 = v1
        self.v2 = v2
        self.helper = None

    def __repr__(self):
        return "%s %s %s" % (self.id, self.v1.id, self.v2.id)

class Poliedro(object):
    def __init__(self, id, vertices, faces):
        self.id = id
        self.vertices = vertices
        self.faces = faces
        self.edges = []

        for i in xrange(len(faces)):
            f = faces[i]
            edges = []

            for j in xrange(0, len(f.vertices)):
                # busco na lista de arestas que já estão no
                # no polígono, para saber qual é uma aresta compatilhada
                # pelo vértice de origem e destino
                e_shared = shared_edge(self.edges, vertices[f.vertices[j-1]-1], vertices[f.vertices[j]-1])
                if e_shared:
                    # caso possua, a aresta simetrica recebe a face 'f'
                    # então checa se a twin possue uma face, se sim,
                    # erro, pois existem mais de uma face compartilhando
                    # a mesma aresta
                    if e_shared.face != None:
                        print "Erro! Aresta com mais de uma face!"
                        return False

                    edges.append(e_shared.id)
                    e_shared.face = f
                    # e a primeira aresta da face é a aresta compartilhada
                    # caso não tenha sido inciada
                    if f.inner == None:
                        f.inner = e_shared
                else:
                    e = Edge(len(self.edges)+1, vertices[f.vertices[j-1]-1], vertices[f.vertices[j]-1], f)
                    e_twin = Edge(len(self.edges)+2, vertices[f.vertices[j]-1], vertices[f.vertices[j-1]-1], None)
                    e.twin = e_twin
                    e_twin.twin = e
                    self.edges.append(e)
                    edges.append(e.id)
                    self.edges.append(e_twin)

            for j in xrange(0, len(edges)):
                self.edges[edges[j-1]-1].next = self.edges[edges[j]-1]
                self.edges[edges[j]-1].prev   = self.edges[edges[j-1]-1]

            # a face recebe como a aresta interna a penúltima
            # aresta criada, para casos em que não tenha aresta
            # compartilhada
            if f.inner == None:
                f.inner = self.edges[-2]




#-----------------------------------------------#
# Verifica se a aresta v1->v2 existe
# Entrada: uma lista de aresta, o vértice de origem
#          e o vértice de destino
# Saida: a aresta v1->v2,
#        false caso nao exista
#-----------------------------------------------#
def shared_edge(edges, v1, v2):
    for e in edges:
        if e.v1.id == v1.id and e.v2.id == v2.id:
            return e
    return False

def show_data(p):
    for f in p.faces:
        print f.inner.id
    for e in p.edges:
        print e.orig, e.twin.id, e.face.id, e.next.id, e.prev.id
    return True
