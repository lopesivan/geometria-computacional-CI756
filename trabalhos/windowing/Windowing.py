# coding=UTF-8
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

class RangeTree(object):
    def __init__(self, P):
        #T = ArvBinBusca( coordenada_y(P) )
        T = ArvBinBusca( P, 1 )
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

def insert(node, point):
    if not node:
        n = Node( point.x, point )
        print n
        return n
    else:
        if node.key < point.x:
            node.right = insert( node.right, point )
        else:
            node.left = insert( node.left, point )

    node.height = max(height(node.left), height(node.right)) + 1

    balance = get_balance(node)
    
    if balance > 1 and point.x < node.left.key:
        return rot_right(node.right)
    if balance > 1 and point.x > node.left.key:
        return rot_left_right(node)
    
    if balance < -1 and point.x > node.right.key:
        return rot_left(node)
    if balance < -1 and point.x < node.right.key:
        return rot_right_left(node)

    return node

def rot_right(y):
    x = y.left
    y.left = x.right
    x.right = y

    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1

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
    return rot_left(n)

def rot_right_left(n):
    n.right = rot_right(n.right)
    return rot_left(n)
#-----------------------------------------------#
# Entrada: uma coleção de pontos, e um booleano
#          indicando por qual coordenada será 
#          usada como chave (true para eixo x)
# Saída: uma arvore binária balanceada
#-----------------------------------------------#
class ArvBinBusca(object):
    def __init__(self, P, x_coord):
        self.root = None
        for point in P:
            insert( self.root, point )

                

def imprime_arv(node):
    if not node:
        return
    imprime_arv(node.left)
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

def coordenada_y(P):
    P_y = []
    for point in P:
        P_y.append( point.y )
    return P_y