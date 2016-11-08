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


class Poligono(object):
    def __init__(self, vertices):

        self.vertices = vertices
        self.edges = []
        self.faces = []

        # inicia a face interna e externa
        outer_face = Face(0, None)
        inner_face = Face(1, None)

        # coloca na lista de faces do poligono
        self.faces.append(outer_face)
        self.faces.append(inner_face)

        # forma o poligono na ordem anti horária
        for i in xrange(0, len(vertices)):

            # cria as arestas
            if i < len(vertices)-1:
                e = Edge(i+1,vertices[i], vertices[i+1], inner_face)
                e_twin = Edge(-(i+1), vertices[i+1], vertices[i], outer_face)

                # face apota para primeira aresta criada
                if self.faces[1].inner == None:
                    self.faces[1].inner = e
                # a face externa aponta para a twin dela
                if self.faces[0].inner == None:
                    self.faces[0].inner = e_twin

                # insere a nova aresta na estrutura do poligono
                # não adiciono a semi-aresta externa
                self.edges.append(e)
                self.vertices[i].edge = e
                self.edges[i].twin = e_twin

        # cria a última aresta
        e = Edge(len(vertices), vertices[len(vertices)-1], vertices[0], inner_face)
        # e a última semi-aresta externa do polígono
        e_twin = Edge(-len(vertices), vertices[0], vertices[len(vertices)-1], outer_face)
        self.edges.append(e)
        self.vertices[len(vertices)-1].edge = e
        self.edges[len(vertices)-1].twin = e_twin

        for i in xrange(0, len(vertices)):
            # cria a dcel
            self.edges[i-1].prox = self.edges[i]
            self.edges[i-1].twin.prox = self.edges[i].twin
            self.edges[i].ant = self.edges[i-1]
            self.edges[i].twin.ant = self.edges[i-1].twin

            # calcula o angulo de cada vértice do polígono
            p2 = self.edges[i].twin.orig
            ref = self.edges[i].orig
            p1 = self.edges[i].ant.orig
            x1, y1 = p1.x - ref.x, p1.y - ref.y
            x2, y2 = p2.x - ref.x, p2.y - ref.y
            ref.theta = theta(x1, y1, x2, y2)



#-----------------------------------------------#
# Função que retorna o angulo formado pela aresta
# e a aresta anterior
# Entrada: uma aresta 'e'
# Saida: o angulo formado por 'e' e 'e.ant'
#-----------------------------------------------#
def angulo(e):
    p2 = e.v2
    ref = e.orig
    p1 = e.ant.orig

    x1, y1 = p1.x - ref.x, p1.y - ref.y
    x2, y2 = p2.x - ref.x, p2.y - ref.y
    return theta(x1,y1,x2,y2)
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
def theta(x1, y1, x2, y2):
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
# Entrada: um Poligono p
# Saída: p com arestas dividindo em sub-poligonos
#        monotônicos
#-----------------------------------------------#
def monotone_decomposition(p):
    status = []
    D = []
    Q = p.vertices[:]
    quick_order_y(Q, 0, len(Q)-1)
    while Q:
        v = Q.pop()
        handle_vertex(p, v, status)

#-----------------------------------------------#
# Lida com cada tipo de vertice, tal como descrito
# no livro do Berg et al.
# Entrada: um vértice
# Saída: a função apropriada para cada tipo de
#        vértice
#-----------------------------------------------#
def handle_vertex(p, v, status):
    # vertice do tipo start
    if abaixo(v, p.vertices[v.id-2]) and abaixo(v, p.vertices[v.id % len(p.vertices)]) and v.theta < 180:
        v.tipo = 'start'
        v.edge.helper = p.vertices[v.id-1]
        status.append(v.edge)

    # vertice do tipo end
    if acima(v, p.vertices[v.id-2]) and acima(v, p.vertices[v.id % len(p.vertices)]) and v.theta < 180:
        v.tipo = 'end'
        if v.edge.ant.helper.tipo == 'merge':
            insere_diagonal(p, v, v.edge.ant.helper)
        if v.edge.ant in status: status.remove(v.edge.ant)

    # vertice do tipo split
    if abaixo(v, p.vertices[v.id-2]) and abaixo(v, p.vertices[v.id % len(p.vertices)]) and v.theta > 180:
        # caso seja um split, insere uma aresta ligando o vertice
        # e o helper anterior
        v.tipo = 'split'
        aresta = esquerda(status, v)
        insere_diagonal(p, v, aresta.helper)
        aresta.helper = v
        v.edge.helper = v
        status.append(v.edge)

    # vertice do tipo merge
    if acima(v, p.vertices[v.id-2]) and acima(v, p.vertices[v.id % len(p.vertices)]) and v.theta > 180:
        v.tipo = 'merge'
        if v.edge.ant.helper and v.edge.ant.helper.tipo  == 'merge':
            insere_diagonal(p, v, v.edge.ant.helper)
        status.remove(p.edges[v.id-2])
        aresta = esquerda(status, v)
        if aresta.helper.tipo == 'merge':
            insere_diagonal(p, v, aresta.helper)
        aresta.helper = v

    # vertice normal
    if (abaixo(v, p.vertices[v.id-2]) and acima(v, p.vertices[v.id % len(p.vertices)])) or (abaixo(v, p.vertices[v.id % len(p.vertices)]) and acima(v, p.vertices[v.id-2])):
        v.tipo = 'regular'
        # Caso o interior do poligono esteja para direita
        if interior_dir(v):
            # caso o helper da aresta for do tipo merge, insere uma diagonal em D
            if v.edge.ant.helper.tipo == 'merge':
                insere_diagonal(p, v, v.edge.ant.helper)
            if p.edges[v.id-2] in status: 
                status.remove(p.edges[v.id-2])
            v.edge.helper = v
            status.append(v.edge)
        else:
            aresta = esquerda(status, v)
            # caso o helper da aresta for do tipo merge, insere uma diagonal em D
            if aresta.helper.tipo == 'merge':
                insere_diagonal(p, v, aresta.helper)
            aresta.helper = v
    return

#-----------------------------------------------#
# Insere uma diagonal do vertice ao helper em D
# Entrada: um vertice e o helper
# Saída: insere a aresta formada pelos dois vertices
#        em D
#-----------------------------------------------#
def interior_dir(v):
    if v.edge.v2.y > v.y:
        return False
    return True

#-----------------------------------------------#
# Diz se a face é a face de um triangulo
# Entrada: uma face do poligono
# Saída: True se a face for um triangulo
#        False caso contrário
#-----------------------------------------------#
def triangulo(f):
    e = f.inner
    v1 = e.prox.prox.v2.id
    v2 = e.v1.id
    if v1 == v2:
        return True
    else:
        return False

#-----------------------------------------------#
# Insere diagonais no poligono monotônico para
# triangular
# Entrada: poligono p
# Saida: um poligono triangulado
#-----------------------------------------------#
def triangulate(p):
    # uma fila Q
    Q = p.faces[1:]

    while Q:
        f = Q.pop(0)
        # 'e' é a aresta inicial da face 'f'
        e = f.inner

        # caso não seja um triangulo, insere uma diagonal
        if not triangulo(f):

            # se o angulo formado entre os vertices for maior que
            # 180, significa que a diagonal ficará fora do poligono
            # então troca até pegar uma 'ponta'
            while angulo(e) >= 180:
                e = e.ant
                f.inner = e

            # insere uma diagonal para fechar um triangulo
            ear_clipping(p, e, e.ant)

            # adiciona a nova face na fila
            Q.append(p.faces[-1])
    return True
    
#def triangulate_monotone(p):


#-----------------------------------------------#
# Insere uma diagonal que forma um triangulo,
# parecido com insere_diagonal()
# Entrada: o poligono e a aresta inicial da face
# Saída: o poligono dividido em dois
#-----------------------------------------------#
def ear_clipping(p, e, e_helper):
    v = e.prox.orig
    helper = e.ant.orig
    f = e.face
    # cria uma nova face
    new_face = Face(len(p.faces), None)
    # cria a diagonal e sua twin
    diagonal = Edge(len(p.edges)+1, v, helper, f)
    twin = Edge(len(p.edges)+2, helper, v, new_face)

    # a proxima da diagonal, tem a mesma face que a aresta do helper
    # a anterior também
    diagonal.prox = e.ant
    diagonal.ant  = e
    # a twin da diagonal recebe a nova face
    twin.prox = e.prox
    twin.ant  = e.ant.ant


    e.ant.ant.prox = twin
    e.ant.ant = diagonal
    e.prox.ant = twin
    e.prox = diagonal

    # a nova face é a face associada à 'twin' da nova diagonal
    new_face.inner = twin

    diagonal.twin = twin
    twin.twin = diagonal

    # atualiza as faces que as arestas adicionadas apontam
    diagonal.face = f
    diagonal.prox.face = f
    diagonal.ant.face  = f
    # para as semi-arestas correspondentes também
    twin.face = new_face
    twin.prox.face = new_face
    twin.ant.face  = new_face

    p.edges.append(diagonal)
    p.edges.append(twin)
    p.faces.append(new_face)

#-----------------------------------------------#
# Insere uma diagonal do vertice ao helper no poligono
# Entrada: o poligono, um vertice e o helper
# Saída: insere a aresta do vertice ao helper no
#        poligono
#-----------------------------------------------#
#def insere_diagonal(p, v.edge.ant, helper.edge)
def insere_diagonal(p, v, helper):
    print  v, helper
    diag_prox = helper.edge #e_helper
    diag_ant  = v.edge.ant
    twin_prox = v.edge #e
    twin_ant  = helper.edge.ant

    # cria uma nova face
    new_face = Face(len(p.faces), None)
    # cria a diagonal e sua twin
    diagonal = Edge(len(p.edges)+1, v, helper, diag_prox.face)
    twin = Edge(len(p.edges)+2, helper, v, new_face)

    # a proxima da diagonal, tem a mesma face que a aresta do helper
    diagonal.prox = diag_prox #e_helper
    diag_prox.ant = diagonal #e_helper.ant = diagonal

    # a anterior também
    diagonal.ant  = diag_ant #diagonal.ant = e.ant
    diag_ant.prox = diagonal #

    # a twin da diagonal recebe a nova face
    twin.prox = twin_prox
    twin_prox.ant = twin
    twin.ant  = twin_ant
    twin_ant.prox = twin

    # a nova face é a face associada à 'twin' da nova diagonal
    new_face.inner = twin
    twin_prox.face.inner = diagonal

    diagonal.twin = twin
    twin.twin = diagonal

    p.edges.append(diagonal)
    p.edges.append(twin)
    p.faces.append(new_face)

    v.edge.ant = diagonal.twin
    helper.edge = diagonal.twin

    # atualiza as arestas para apontarem para a nova face
    inicio = twin.v1
    e = twin.prox
    while e.v1 != inicio:
        e.face = new_face
        e = e.prox
    return True

#-----------------------------------------------#
# Função para encontrar a aresta helper imediatamente
# à esquerda do vertice v
# Entrada: um lista, um vertice
# Saída: a aresta à esquerda de v
#-----------------------------------------------#
def esquerda(status, v):
    menor = -1000000
    ej = None
    for e in status:
        d = distancia(e, v)
        if d!= 0 and d > menor:
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
