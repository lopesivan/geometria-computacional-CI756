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
        self.info = point
        self.left = None
        self.right = None
        self.tree_assoc = None
        self.bal = 0
#-----------------------------------------------#
# Entrada: uma coleção de pontos, e um booleano
#          indicando por qual coordenada será 
#          usada como chave (true para eixo x)
# Saída: uma arvore binária balanceada
#-----------------------------------------------#
class ArvBinBusca(object):
    def __init_(self, P, x_coord):
        root = None
        for point in P:
            insert( root, point )

    def insert(self, node, point):
        if not node:
            return node = Node( point.x, point )
        else:
            if node.key <= point.x:
                insert( node.right, point )
                node.bal += 1
            else:
                insert( node.left, point )
                node.bal -= 1

    def rot_left(n):
        x = n.left
        n.left = x.right
        x.right = n
        return x

    def rot_right(n):
        x = n.right
        n.right = x.left
        x.left = n 
        return x

    def rot_left_right(n):
        n.left = rot_right(n.left)
        return rot_left(n)

    def rot_right_left():
        n.right = rot_left(n.right)
        return rot_right(n)

def coordenada_y(P):
    P_y = []
    for point in P:
        P_y.append( point.y )
    return P_y