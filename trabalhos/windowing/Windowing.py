# coding=UTF-8

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%s,%s)" % (self.x, self.y)

class Segment(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Window(object):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def RangeTree(P):
    #T = ArvBinBusca( coordenada_y(P) )
    T = ArvBinBusca( P, 0 )
    if len(P) == 0:
        return 
    if len(P) == 1:
        v = Node( P[0].x, P[0] )
        v.tree_assoc = T.root 
    else:
        left, right = split(P)
        x_mid = left.pop()
        v_left = RangeTree(left)
        v_right = RangeTree(right)
        v = Node( x_mid.x, x_mid )
        v.left = v_left
        v.right = v_right
    return v

#-----------------------------------------------#
# Função que divide uma coleção de pontos em
# menores que a mediana das coordenas-x
#
# Entrada: uma coleção de pontos
# Saída: duas listas de pontos, P_left e P_right
#-----------------------------------------------#
def split(points):
    left = []
    right = []

    x_mid = median(points)

    for p in points:
        if p.x <= x_mid:
            left.append(p)
        else:
            right.append(p)

    return left, right

def median(points):
    total_x = 0
    for p in points:
        total_x += p.x
    return total_x/len(points)

def coordenada_y(P):
    P_y = []
    for point in P:
        P_y.append( point.y )
    return P_y


#--------- Funções para árvore AVL -------------#

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
#-----------------------------------------------#
# Entrada: uma coleção de pontos, e um booleano
#          indicando por qual coordenada será 
#          usada como chave (true para eixo x)
# Saída: uma arvore binária balanceada
#-----------------------------------------------#
class ArvBinBusca(object):
    def __init__(self, P, x_coord):
        self.root = None
        if x_coord:
            for point in P:
                self.root = insert_x( self.root, point )
        else:
            for point in P:
                self.root = insert_y( self.root, point )

#-----------------------------------------------#
# Função recursiva para inserir um ponto na árvore
# com base na coordenada y
# Entrada: o nó raiz e o ponto a ser inserido
# Saída: uma arvore binária balanceada
#-----------------------------------------------#
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

#-----------------------------------------------#
# Função recursiva para inserir um ponto na árvore
# com base na coordenada x
# Entrada: o nó raiz e o ponto a ser inserido
# Saída: uma arvore binária balanceada
#-----------------------------------------------#
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

#-----------------------------------------------#
# Funções helpers para manter balanceamento da AVL
#-----------------------------------------------#
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
    if node.tree_assoc:
        imprime_arv(node.tree_assoc)
    print node
    imprime_arv(node.right)

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def height(node):
    if not node:
        return 0
    return node.height
