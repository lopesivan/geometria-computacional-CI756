# coding=UTF-8
import math
from math import sqrt
from math import acos, cos, degrees

class Ponto(object):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

        self.prox = None
        self.ant = None
        self.edge = None
        self.tipo = None
        self.theta = None

    def __repr__(self):
        return "%s (%s,%s) \'tipo\': \'%s\'" % (self.id, self.x, self.y, self.tipo)

class Face(object):
    def __init__(self, id, inner, outer):
        self.id = id
        self.inner = inner
        self.outer = outer
    def __repr__(self):
        return "%s in: %s out: %s" % (self.id, self.inner, self.outer)

class Edge(object):
    def __init__(self, id, v1, v2, face):
        self.id = id
        self.orig = v1
        self.face = face
        self.twin = None
        self.prox = None
        self.ant = None
        self.v1 = v1
        self.v2 = v2
        self.helper = None

    def __repr__(self):
        return "%s {%s, %s}" % (self.id, self.v1.id, self.v2.id)
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
            print "Error! Divisao por 0!"
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
    def origin(self):
        return self.v1

    def next(self):
        return self.orig.edge


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
        self.monotone = []
        self.edges = []
        self.vertices = vertices
        self.faces = []
        outer_face = Face(0, None, None)
        inner_face = Face(1, None, None)
        self.faces.append(outer_face)
        self.faces.append(inner_face)


        # forma o poligono na ordem em que foi dada na entrada
        for i in xrange(0, len(vertices)):
            # incia os vertices
            self.vertices[i-1].prox = self.vertices[i]
            self.vertices[i].ant = vertices[i-1]

            # inicia as arestas
            if i < len(vertices)-1:
                e = Edge(i+1,vertices[i], vertices[i+1], inner_face)
                e_twin = Edge(-(i+1), vertices[i+1], vertices[i], outer_face)

                # inicia as faces
                if self.faces[1].inner == None:
                    self.faces[1].inner = e
                if self.faces[0].inner == None:
                    self.faces[0].inner = e_twin

                # insere a nova aresta na estrutura do poligono
                self.edges.append(e)
                self.vertices[i].edge = e
                self.edges[i].twin = e_twin

        # inicia a última aresta
        e = Edge(len(vertices), vertices[len(vertices)-1], vertices[0], inner_face)
        e_twin = Edge(-len(vertices), vertices[0], vertices[len(vertices)-1], outer_face)
        self.edges.append(e)
        self.vertices[len(vertices)-1].edge = e
        self.edges[len(vertices)-1].twin = e_twin

        for i in xrange(0, len(vertices)):
            self.edges[i-1].prox = self.edges[i]
            self.edges[i-1].twin.prox = self.edges[i].twin
            self.edges[i].ant = self.edges[i-1]
            self.edges[i].twin.ant = self.edges[i-1].twin
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
        #for i in xrange(0,len(self.vertices)):
        for e in self.edges:
            p2 = e.twin.orig
            ref = e.orig
            p1 = e.ant.orig

            x1, y1 = p1.x - ref.x, p1.y - ref.y
            x2, y2 = p2.x - ref.x, p2.y - ref.y
            ref.theta = theta(x1, y1, x2, y2)


        return True

#-----------------------------------------------#
# Ordenação de vértices pela coordenada y, baseado
# em quicksort
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
def theta(x1, y1, x2, y2): # adaptar para receber um segmento
    dot = (x1 * x2) + (y1 * y2)
    denom = sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))
    if x1 * y2 < x2 * y1:
        angulo = math.degrees(acos(dot/denom))
    else:
        angulo = 360.0 - math.degrees(acos(dot/denom))
    return int(angulo)


#-----------------------------------------------#
# Função que implementa sweep line para dividir
# o poligono em pedaços monotônicos
# Entrada: um Poligono
# Saída: uma subdivisão em D
#-----------------------------------------------#
def sweep(p):
    status = []
    D = []
    Q = p.vertices[:]
    quick_order_y(Q, 0, len(Q)-1)
    while Q:
        v = Q.pop()
        p.monotone.append(v)
        handle_vertex(p, v, status)

#-----------------------------------------------#
# Lida com cada tipo de vertice
# Entrada: um vértice
# Saída: a função apropriada para cada tipo de
#        vértice
#-----------------------------------------------#
def handle_vertex(p, v, status):
    # vertice do tipo start
    if abaixo(v, v.ant) and abaixo(v, v.prox) and v.theta < 180:
        v.tipo = 'start'
        p.edges[v.id-1].helper = p.vertices[v.id-1]
        status.append(p.edges[v.id-1])

    # vertice do tipo end
    if acima(v, v.ant) and acima(v, v.prox) and v.theta < 180:
        v.tipo = 'end'
        if p.edges[v.id-2].helper.tipo == 'merge':
            insere_diagonal(p, v, p.edges[v.id-2].helper)
        status.remove(p.edges[v.id-2])

    # vertice do tipo split
    if abaixo(v, v.ant) and abaixo(v, v.prox) and v.theta > 180:
        v.tipo = 'split'
        aresta = esquerda(status, v)
        insere_diagonal(p, v, aresta.helper)
        aresta.helper = v
        p.edges[v.id-1].helper = v
        status.append(p.edges[v.id-1])

    # vertice do tipo merge
    if acima(v, v.ant) and acima(v, v.prox) and v.theta > 180:
        v.tipo = 'merge'
        if p.edges[v.id-2].helper.tipo == 'merge':
            insere_diagonal(p, v, p.edges[v.id-2].helper)
        status.remove(p.edges[v.id-2])
        aresta = esquerda(status, v)
        if aresta.helper.tipo == 'merge':
            insere_diagonal(p, v, aresta.helper)
        aresta.helper = v

    # vertice normal
    if (abaixo(v, v.ant) and acima(v, v.prox)) or (abaixo(v, v.prox) and acima(v, v.ant)):
        v.tipo = 'regular'
        # Caso o interior do poligono esteja para direita
        if interior_dir(v):
            # caso o helper da aresta for do tipo merge, insere uma diagonal em D
            if p.edges[v.id-2].helper.tipo == 'merge':
                insere_diagonal(p, v, p.edges[v.id-2].helper)
            status.remove(p.edges[v.id-2])
            p.edges[v.id-1].helper = v
            status.append(p.edges[v.id-1])
        else:
            aresta = esquerda(status, v)
            # caso o helper da aresta for do tipo merge, insere uma diagonal em D
            if aresta.helper.tipo == 'merge':
                insere_diagonal(p, v, p.edges[v.id-1].helper)
            aresta.helper = v
    return

#-----------------------------------------------#
# Insere uma diagonal do vertice ao helper em D
# Entrada: um vertice e o helper
# Saída: insere a aresta formada pelos dois vertices
#        em D
#-----------------------------------------------#
def interior_dir(v):

    return True


#-----------------------------------------------#
# Insere uma diagonal do vertice ao helper em D
# Entrada: um vertice e o helper
# Saída: insere a aresta formada pelos dois vertices
#        em D
#-----------------------------------------------#
def insere_diagonal(p, v, helper):
    # insere a aresta (v_i, helper) em D
    # isso faz parte do mapeamento dos subpoligonos
    new_face = Face(len(p.faces), None, None)

    diagonal = Edge(len(p.edges)+1, v, helper, new_face)
    new_face.inner = diagonal
    print 'diagonal ', diagonal
    diagonal.prox = p.edges[helper.edge.id-1]# helper.edge #
    print 'diagonal.prox ', diagonal.prox
    diagonal.ant  = p.edges[v.edge.ant.id-1]#v.edge.ant #
    print 'diagonal.ant ',diagonal.ant
    twin = Edge(len(p.edges)+2, helper, v, p.edges[helper.id-2].face)
    print 'twin ',twin
    twin.prox = p.edges[v.edge.id-1]#v.edge #
    print 'twin.prox ',twin.prox
    twin.ant  = p.edges[helper.edge.ant.id-1] #helper.edge.ant #
    print 'twin.ant ',twin.ant
    diagonal.twin = twin
    twin.twin = diagonal

    p.edges.append(diagonal)
    p.edges.append(twin)
    p.faces.append(new_face)


    p.edges[helper.edge.id-1].ant.prox = diagonal
    print 'p.edges[helper.edge.id-1].ant ', p.edges[helper.edge.id-1].ant
    p.edges[helper.edge.ant.id-1].prox = diagonal.twin
    print 'p.edges[helper.edge.ant.id-1].prox ', p.edges[helper.edge.ant.id-1].prox
    p.edges[v.edge.ant.id-1].prox = diagonal
    print 'p.edges[v.edge.ant.id-1].prox ', p.edges[v.edge.ant.id-1].prox
    p.edges[v.edge.id-1].ant = diagonal.twin
    print 'p.edges[v.edge.id-1].ant ', p.edges[v.edge.id-1].ant


    v.edge.ant = diagonal.twin
    print 'v.edge ', v.edge
    helper.edge = diagonal.twin
    print 'helper.edge ', helper.edge
    p.vertices[helper.id-1].edge = helper.edge # p.edges[helper.id-1]
    p.vertices[v.id-1].edge = v.edge # p.edges[v.id-1]

    #print diagonal, new_face
    print 'arestas de v',p.edges[v.id-1], p.edges[v.id-2]
    print 'arestas de helper',  p.edges[helper.id-1], p.edges[helper.id-2]
    return True

def monotone_piece(p, diagonal):
    inicio = diagonal.v1
    v = diagonal.v2
    while v != inicio:
        v = v.prox
        return True

#-----------------------------------------------#
# Função para encontrar a aresta imediatamente
# à esquerda do vertice v
# Entrada: um lista, um vertice
# Saída: a aresta à esquerda de v
#-----------------------------------------------#
def esquerda(status, v):
    menor = 1000000
    ej = None
    for e in status:
        d = distancia(e, v)
        if d < menor:
            menor = d
            ej = e
    return ej

#-----------------------------------------------#
# Funções helper
#-----------------------------------------------#
def distancia(e, v):
    num = (e.v2.y - e.v1.y)*v.x - (e.v2.x - e.v1.x)*v.y + e.v2.x * e.v1.y - e.v2.y * e.v1.x
    denom = sqrt( (e.v2.y - e.v1.y)**2 + (e.v2.x - e.v1.x)**2 )
    if denom == 0:
        return False
    else:
        return  num / denom

def abaixo(p, q):
    if (q.y < p.y or (q.y == p.y and q.x > p.x) ):
        return True
    return False

def acima(p, q):
    if (q.y > p.y) or (q.y == p.y and q.x < p.x):
        return True
    return False

def cross_sign(x1, y1, x2, y2):
    return x1 * y2 < x2 * y1

def print_v(vertices):
    for v in vertices:
        print "     ", v, " 0: ", v.theta
        print v.ant, " --- ", v.prox
        print ""

def print_s(arestas):
    for s in arestas:
        print s, '        ', s.twin, '       ', s.v1.edge
        print s.ant, '  ----  ', s.prox

def print_f(faces):
    for f in faces:
        inicio = f.inner
        e = inicio.prox
        i = 0
        print 'olha ai', f
        while e.id != inicio.id and i < 10:
            print e
            e = e.prox
            i = i + 1
        #print f
        #   print f.inner.prox
