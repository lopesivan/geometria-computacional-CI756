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
        self.edge = None
    def __repr__(self):
        return "%s (%s,%s,%s)" % (self.id, self.x, self.y, self.z)

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
        self.next = None
        self.prev = None

    def __repr__(self):
        return "%s origem: %s" % (self.id, self.orig.id)

class Poliedro(object):
    def __init__(self, id, vertices, faces, vertices_faces):
        self.id = id
        self.vertices = vertices
        self.faces = faces
        self.edges = []

        for i in xrange(len(faces)):
            f = faces[i]
            v = vertices_faces.pop(0)
            edges = []

            for j in xrange(0, len(v)):
                # busco na lista de arestas que já estão no
                # no polígono, para saber qual é uma aresta compatilhada
                # pelo vértice de origem e destino
                e_shared = shared_edge(self.edges, vertices[v[j-1]-1], vertices[v[j]-1])
                if e_shared:
                    # caso possua, a semi-aresta recebe a face 'f'
                    # então checa se possue uma face, se sim,
                    # erro, pois existem mais de uma face compartilhando
                    # a mesma semi-aresta, portanto não é orientável
                    if e_shared.face != None:
                        print 'não orientável'
                        exit(1)

                    # guardo o indice da aresta para posteriormente
                    # definir quem é o próximo e o anterior da aresta
                    edges.append(e_shared.id)
                    e_shared.face = f
                    # e a primeira aresta da face é a aresta compartilhada
                    # caso não tenha sido inciada
                    if f.inner == None:
                        f.inner = e_shared
                else:
                    # crio a aresta e sua simétrica
                    e = Edge(len(self.edges)+1, vertices[v[j-1]-1], vertices[v[j]-1], f)
                    e_twin = Edge(len(self.edges)+2, vertices[v[j]-1], vertices[v[j-1]-1], None)
                    e.twin = e_twin
                    e_twin.twin = e

                    # define a aresta do vertice caso não tenha ainda
                    if vertices[v[j-1]-1].edge == None:
                        self.vertices[v[j-1]-1].edge = e

                    # insiro na lista de aresta do poliedro
                    self.edges.append(e)
                    self.edges.append(e_twin)
                    edges.append(e.id)

            for j in xrange(0, len(edges)):
                self.edges[edges[j-1]-1].next = self.edges[edges[j]-1]
                self.edges[edges[j]-1].prev   = self.edges[edges[j-1]-1]

            # a face recebe como a aresta interna a penúltima
            # aresta criada, para casos em que não tenha aresta
            # compartilhada
            if f.inner == None:
                f.inner = self.edges[-2]

#-----------------------------------------------#
# Verifica se o poliedro está aberto
# Entrada: um poliedro
# Saida: True caso esteja aberto,
#        false caso contrário
#-----------------------------------------------#
def aberto(p):
    for e in p.edges:
        if e.face == None:
            return True
    return False

#-----------------------------------------------#
# Verifica se a aresta v1->v2 existe
# Entrada: uma lista de aresta, o vértice de origem
#          e o vértice de destino
# Saida: a aresta v1->v2,
#        false caso nao exista
#-----------------------------------------------#2
def shared_edge(edges, v1, v2):
    for e in edges:
        if e.orig.id == v1.id and e.twin.orig.id == v2.id:
            return e
    return False

def show_data(p, vertices):
    print len(p.vertices), len(p.edges)/2, len(p.faces)
    for v in p.vertices:
        print v.x, v.y, v.z, v.edge.id
    for vertex in vertices:
        print ' '.join( str(v) for v in vertex )
    for f in p.faces:
        print f.inner.id
    for e in p.edges:
        print e.orig.id, e.twin.id, e.face.id, e.next.id, e.prev.id
    return True
