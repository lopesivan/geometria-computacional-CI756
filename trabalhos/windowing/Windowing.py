# coding=UTF-8

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
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

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
        self.segments = []
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
# Função para gerar intervalos elementares para a
# árvore de segmentos
#
# Entrada: uma lista P de pontos
# Saída: intervalos elementares baseados no eixo-x
#---------------------------------------------------#
def interval(P):
    response = []
    response.append(Interval(-float("inf"), P[0].x, False))
    i = 0
    while i < len(P)-1:
        if P[i].x != P[i+1].x:
            response.append(Interval(P[i].x, P[i].x, True))
            response.append(Interval(P[i].x, P[i+1].x, False))
        i += 1
    response.append(Interval(P[-1].x, P[-1].x, True))
    response.append(Interval(P[-1].x, float("inf"), False))
    return response

def SegmentTree(I):
    if len(I) == 1:
        v = IntNode(I[0])
    else:
        left, right = split2(I)

        if left[0].closed and right[-1].closed:
            v = IntNode(Interval(left[0].left, right[-1].right, True))
        # fechado à direita
        if not left[0].closed and right[-1].closed:
            v = IntNode(Interval(left[0].left, right[-1].right, False, 1))
        # fechado à esquerda
        if left[0].closed and not right[-1].closed:
            v = IntNode(Interval(left[0].left, right[-1].right, False, 2))
        if not left[0].closed and not right[-1].closed:
            v = IntNode(Interval(left[0].left, right[-1].right, False))

        l_left = SegmentTree(left)
        l_right = SegmentTree(right)

        v.left = l_left
        v.right = l_right
        v.height = max(height(v.left), height(v.right)) + 1
    return v

def insertSegment(node, s):
    if not node:
        return
    if intervalContained(node.key, s):
        node.segments.append(s)
        return
    else:
        if s.side:
            if node.left:
                if s.upper.x <= node.left.key.right:
                    insertSegment(node.left, s)
            if node.right:
                if s.lower.x >= node.right.key.left:
                    insertSegment(node.right, s)
        else:
            if node.left:
                if s.lower.x <= node.left.key.right:
                    insertSegment(node.left, s)
            if node.right:
                if s.upper.x >= node.right.key.left:
                    insertSegment(node.right, s)

# responde se s é maior ou igual ao intervalo baseado no eixo x
def intervalContained(intvl, s):
    if s.side:
        if intvl.closed:
            if s.upper.x <= intvl.left and intvl.right <= s.lower.x:
                return True
        else:
            if s.upper.x <= intvl.left and intvl.right <= s.lower.x:
                return True
    else:
        if intvl.closed:
            if s.lower.x <= intvl.left and intvl.right <= s.upper.x:
                return True
        else:
            if s.lower.x <= intvl.left and intvl.right <= s.upper.x:
                return True

def querySegmentTree(node, q):
    if leaf(node):
        print node.key
        return

    if node.left.key.closed:
        if q <= node.left.key.right:
            querySegmentTree(node.left, q)
    else:
        if not node.left.key.semiclosed and q < node.left.key.right:
            querySegmentTree(node.left, q)
        if node.left.key.semiclosed == 1 and q <= node.left.key.right:
            querySegmentTree(node.left, q)

    if node.right.key.closed:
        if q >= node.right.key.left:
            querySegmentTree(node.right, q)
    else:
        if not node.right.key.semiclosed and q > node.right.key.left:
            querySegmentTree(node.right, q)
        if node.right.key.semiclosed == 2 and q >= node.right.key.left:
            querySegmentTree(node.right, q)

    return
    
def imprime_intervalos(node):
    if not node:
        print 'folha vazia'
        return
    
    print node.key
    imprime_intervalos(node.left)
    print ' - '
    imprime_intervalos(node.right)


def RangeTree(P):
    T = ArvBinBusca(P, 0)
    if len(P) == 0:
        return
    if len(P) == 1:
        v = Node(P[0].x, P[0])
        v.tree_assoc = T.root
    else:
        #--------------------------------------------#
        # Divide o conjunto de pontos com base na
        # mediana da coordenada x em duas listas, esquerda
        # e direita, onde pontos com coordenada menor
        # que x_mid na esquerda, e maiores à direita
        left, right = split(P)
        # guarda o nó do meio, no caso, o maior da lista
        # da esquerda
        x_mid = left.pop(getRootIndex(left))

        v_left = RangeTree(left)
        v_right = RangeTree(right)
        v = Node(x_mid.x, x_mid)
        v.left = v_left
        v.right = v_right

        # guarda a raiz da árvore balanceada associada
        # no nó do meio
        v.tree_assoc = T.root
        #--------------------------------------------#

        v.height = max(height(v.left), height(v.right)) + 1

    return v

def query2DRangeTree(node, x, x1, y, y1):
    response = []
    v_split = findSplitNode(node, x, x1)
    if leaf(v_split):
        if (x < v_split.point.x and v_split.point.x < x1 and
            y < v_split.point.y and v_split.point.y < y1):
            if not v_split.point.segment.reported:
                response.append(v_split.point.segment.id)
                v_split.point.segment.reported = True
    else:
        if (x < v_split.point.x and v_split.point.x < x1 and
            y < v_split.point.y and v_split.point.y < y1):
            if not v_split.point.segment.reported:
                response.append(v_split.point.segment.id)
                v_split.point.segment.reported = True
        v = v_split.left
        while not leaf(v):
            if x <= v.point.x:
                response.extend(query1DRangeTree(v.tree_assoc, y, y1))
                v = v.left
            else:
                v = v.right
        if v and v.point.segment.reported:
            if (x < v.point.x and v.point.x < x1 and
                y < v.point.y and v.point.y < y1):
                response.append(v.point.segment.id)
                v.point.segment.reported = True

        v = v_split.right
        while not leaf(v):
            if v.point.x <= x1:
                response.extend(query1DRangeTree(v.tree_assoc, y, y1))
                v = v.right
            else:
                v = v.left
        if v and not v.point.segment.reported:
            if (x < v.point.x and v.point.x < x1 and
                y < v.point.y and v.point.y < y1):
                response.append(v.point.segment.id)
                v.point.segment.reported = True

    return response


def query1DRangeTree(node, x, x1):
    response = []
    v_split = findSplitNode(node, x, x1)
    if leaf(v_split):
        if x <= v_split.key and v_split.key <= x1:
            if not v_split.point.segment.reported:
                response.append(v_split.point.segment.id)
                v_split.point.segment.reported = True
    else:
        if x <= v_split.key and v_split.key <= x1:
            if not v_split.point.segment.reported:
                response.append(v_split.point.segment.id)
                v_split.point.segment.reported = True
        #--------------------------------------------#
        # percorre a subárvore à esquerda do nó split
        # e reporta todos os pontos à direita.
        #

        v = v_split.left
        while not leaf(v):
            if x < v.key:
                reportSubtree(v.right, response)
                v = v.left
            else:
                v = v.right
        if v and x <= v.key:
            if not v.point.segment.reported:
                response.append(v.point.segment.id)
                v.point.segment.reported = True
        #
        # semelhante para o limite de x'
        #
        v = v_split.right
        while not leaf(v):
            if v.key <= x1:
                reportSubtree(v.left, response)
                v = v.right
            else:
                v = v.left
        if v and v.key <= x1:
            if not v.point.segment.reported:
                response.append(v.point.segment.id)
                v.point.segment.reported = True
        #
        #--------------------------------------------#
    return response

#---------------------------------------------------#
# Função que concatena recursivamente os nós na
# resposta que será reportada
#
# Entrada: um nó e uma lista de resposta
# Saída: NA
#---------------------------------------------------#
def reportSubtree(node, response):
    if not node:
        return True
    reportSubtree(node.left, response)
    reportSubtree(node.right, response)
    response.append(node)
    return True

#---------------------------------------------------#
# Função que encontra e retorna o nó split
#
# Entrada: nó raiz e um intervalo [x:x']
# Saída: nó split
#---------------------------------------------------#
def findSplitNode(node, x, x1):
    v = node
    while not leaf(v) and (x1 <= v.key or x > v.key):
        if x1 <= v.key:
            v = v.left
        else:
            v = v.right
    return v

#---------------------------------------------------#
# Função que divide uma coleção de pontos em
# menores que a mediana das coordenas-x
#
# Entrada: uma coleção de pontos
# Saída: duas listas de pontos, P_left e P_right
#---------------------------------------------------#
def split(points):
    left = []
    right = []
    if len(points) % 2 == 0:
        x_mid = len(points)/2
    else:
        x_mid = (len(points)-1)/ 2

    i = 0

    while i <= x_mid:
        left.append(points[i])
        i += 1
    while i < len(points):
        right.append(points[i])
        i += 1

    return left, right

def split2(points):
    left = []
    right = []
    if len(points) % 2 == 0:
        x_mid = len(points)/2
    else:
        x_mid = (len(points)-1)/ 2

    i = 0

    while i < x_mid:
        left.append(points[i])
        i += 1
    while i < len(points):
        right.append(points[i])
        i += 1

    return left, right

#---------------------------------------------------#
# Função que devolve o maior elemento de uma lista
# de pontos com base na coordenada-x
#
# Entrada: uma coleção de pontos
# Saída: índice do maior elemento
#---------------------------------------------------#
def getRootIndex(t):
    maior = 0
    i = 0
    for e in t:
        if t[maior].x < e.x:
            maior = i
        i += 1
    return maior

#---------------------------------------------------#
# Função identifica se o nó é folha
#
# Entrada: um nó
# Saída: True se for um nó folha,
#        False caso contrário
#---------------------------------------------------#
def leaf(node):
    if not node or (not node.left and not node.right):
        return True
    return False

def coordenada_y(P):
    P_y = []
    for point in P:
        P_y.append(point.y)
    return P_y




#---------------------------------------------------#
#------------- Funções para árvore AVL -------------#
#---------------------------------------------------#

#---------------------------------------------------#
# Entrada: uma coleção de pontos, e um booleano
#          indicando por qual coordenada será 
#          usada como chave (true para eixo x)
# Saída: uma arvore binária balanceada
#---------------------------------------------------#
class ArvBinBusca(object):
    def __init__(self, P, x_coord):
        self.root = None
        if x_coord:
            for point in P:
                self.root = insert_x( self.root, point )
        else:
            for point in P:
                self.root = insert_y( self.root, point )
    def __repr__(self):
        return "%s (%s,%s) %s" % (self.root.key, self.root.point.x, self.root.point.y, self.root.height)

#---------------------------------------------------#
# Função recursiva para inserir um ponto na árvore
# com base na coordenada y
#
# Entrada: o nó raiz e o ponto a ser inserido
# Saída: uma arvore binária balanceada
#---------------------------------------------------#
def insert_y(node, point):
    if not node:
        n = Node( point.y, point )
        return n
    else:
        if node.key < point.y:
            node.right = insert_y( node.right, point )
        else:
            node.left = insert_y( node.left, point )

    node.height = max(height(node.left), height(node.right)) + 1

    balance = get_balance(node)
    
    if balance > 1 and point.y < node.left.key:
        return rot_right(node)
    if balance > 1 and point.y > node.left.key:
        return rot_left_right(node)
    
    if balance < -1 and point.y > node.right.key:
        return rot_left(node)
    if balance < -1 and point.y < node.right.key:
        return rot_right_left(node)

    return node

#---------------------------------------------------#
# Função recursiva para inserir um ponto na árvore
# com base na coordenada x
#
# Entrada: o nó raiz e o ponto a ser inserido
# Saída: uma arvore binária balanceada
#---------------------------------------------------#
def insert_x(node, point):
    if not node:
        n = Node( point.x, point )
        return n
    else:
        if node.key < point.x:
            node.right = insert_x( node.right, point )
        else:
            node.left = insert_x( node.left, point )

    node.height = max(height(node.left), height(node.right)) + 1

    balance = get_balance(node)
    
    if balance > 1 and point.x < node.left.key:
        return rot_right(node)
    if balance > 1 and point.x > node.left.key:
        return rot_left_right(node)
    
    if balance < -1 and point.x > node.right.key:
        return rot_left(node)
    if balance < -1 and point.x < node.right.key:
        return rot_right_left(node)

    return node

#---------------------------------------------------#
# Funções helpers para manter balanceamento da AVL
#---------------------------------------------------#
def rot_right(y):
    x = y.left
    y.left = x.right
    x.right = y

    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    return x

def rot_left(y):
    x = y.right
    y.right = x.left
    x.left = y 

    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1

    return x

def rot_left_right(n):
    n.left = rot_left(n.left)
    return rot_right(n)

def rot_right_left(n):
    n.right = rot_right(n.right)
    return rot_left(n)

def imprime_arv(node):
    if not node:
        return
    imprime_arv(node.left)
    esp = ''
    for i in xrange(node.height):
        esp = esp + "    "
    print esp, node
    imprime_arv(node.right)

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def height(node):
    if not node:
        return 0
    return node.height
