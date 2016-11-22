#---------------------------------------------------#
# Entrada: uma lista I de intervalos elementares
# Saida: a raiz de uma arvore de intervalos 
#---------------------------------------------------#
def intervalTree(I):
    if len(I) == 1:
        # instancia um no' 
        v = IntNode(I[0])
    else:
        left, right = split2(I)

        # define se o intervalo do no' corrente e' fechado, 
        if left[0].closed and right[-1].closed:
            i = Interval(left[0].left, right[-1].right, True)
            v = IntNode(i)
        # fechado 'a direita 
        if not left[0].closed and right[-1].closed:
            i =  Interval(left[0].left, right[-1].right, False, LEFT)
            v = IntNode(i)
        # fechado 'a esquerda,
        if left[0].closed and not right[-1].closed:
            i = Interval(left[0].left, right[-1].right, False, RIGHT)
            v = IntNode(i)
        # ou aberto
        if not left[0].closed and not right[-1].closed:
            i = Interval(left[0].left, right[-1].right, False)
            v = IntNode(i)

        l_left = intervalTree(left)
        l_right = intervalTree(right)

        v.left = l_left
        v.right = l_right
        # atualiza a altura da arvore
        v.height = max(height(v.left), height(v.right)) + 1
    return v