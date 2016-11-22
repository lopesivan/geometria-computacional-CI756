#---------------------------------------------------#
# Entrada: o no' raiz, um segmento de busca vertical e 
#          um array para armazenar a resposta
# Saida: NA
#---------------------------------------------------#
def querySegmentTreeVertical(node, q, response):
    if leaf(node):
        response += reportIntersectionVertical(node.segments, q)
        return

    if belongsLeftX(node, q):
        response += reportIntersectionVertical(node.segments, q)
        querySegmentTreeVertical(node.left, q, response)

    if belongsRightX(node, q):
        response += reportIntersectionVertical(node.segments, q)
        querySegmentTreeVertical(node.right, q, response)