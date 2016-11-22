#---------------------------------------------------#
# Entrada: uma lista I de intervalos elementares
# Saida: uma arvore de segmentos
#---------------------------------------------------#
def segmentTreeX(I, segments, vertical):
    root = intervalTree(I)
    for s in segments:
            insertSegmentVertical(root, s)
    return root

#---------------------------------------------------#
# Entrada: o no' raiz da arvore e o segmento
# Saida: NA
#---------------------------------------------------#
def insertSegmentVertical(node, s):
    if not node:
        return
    if intervalContainedX(node.key, s):
        node.segments = insert_y(node.segments, s.upper)
    else:
        if node.left:
            if s.left.x <= node.left.key.right:
                insertSegmentVertical(node.left, s)
        if node.right:
            if s.right.x >= node.right.key.left:
                insertSegmentVertical(node.right, s)