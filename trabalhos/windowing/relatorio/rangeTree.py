#---------------------------------------------------#
# Entrada: um conjunto de pontos
# Saida: no' raiz da arvore
#---------------------------------------------------#
def RangeTree(P):
    T = avlTree(P)
    if len(P) == 0:
        return
    if len(P) == 1:
        v = Node(P[0].x, P[0])
        v.tree_assoc = T
    else:
        left, right = split(P)
        # faco do no' mediano a raiz da sub-arvore 
        x_mid = left.pop(-1)
        v = Node(x_mid.x, x_mid)
        # chamo recursivamente para esquerda 
        v_left = RangeTree(left)
        # e direita
        v_right = RangeTree(right)
        # atualizo os ponteiros para as sub-arvores
        v.left = v_left
        v.right = v_right
        # associo a estrutura do subconjunto canonico
        v.tree_assoc = T
        # e atualizo a altura
        v.height = max(height(v.left), height(v.right)) + 1
    return v