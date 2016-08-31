class Vertice(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s,%s)" % (self.x,self.y)

class Segmento(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __str__(self):
        return "{ %s , %s }"%(self.v1,self.v2)
    #-----------------------------------------------#
    # Calcula a interseccao de dois segmentos
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
            print "Error! Divisao por 0 nao permitida!"
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
    def helper_split(self):
        return True

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
        self.segments = []
        quick_order_y(vertices, 0, len(vertices)-1)
        self.vertices = vertices
    
        for i in xrange(len(vertices) - 1):
            self.segments.append(Segmento(vertices[i], vertices[i+1]))
        self.segments.append(Segmento(vertices[len(vertices)-1], vertices[0]))
        
    #-----------------------------------------------#
    # Decompoe o poligono em trapezoides (horizontal
    # visibility map [1])
    # Entrada: poligono simples P 
    # Saida: uma divisao de P em poligono monotonico
    #-----------------------------------------------#
    def monotone_decomposition(self):
        print "monotone_decomposition()"
        print "..."
        Q = self.vertices[:]
        quick_order_y(Q, 0, len(Q)-1)
        print_v(Q) 
        while Q:
            Q.pop()
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
    # Saida: uma classificacao dos vertices
    #-----------------------------------------------#    
    def classify(self):
        return True


def quick_order_y(v, esq, dir):
    print "quicksort()"
    print "..."
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


def print_v(vertices):
    print "print_v()"
    print "..."
    for v in vertices:
        print v        

def print_s(segments):
    print "print_s()"
    print "..."
    for s in segments:
        print s