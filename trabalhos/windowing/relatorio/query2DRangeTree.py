#---------------------------------------------------#
# Entrada: a raiz da Range Tree e uma janela
# Saida: pontos que estao dentro da janela
#---------------------------------------------------#
def query2DRangeTree(node, x, x1, y, y1):
    response = []
    v_split = findSplitNode(node, x, x1)
    if leaf(v_split):
        if inside(v_split, x, x1, y, y1):
            if not v_split.point.segment.reported:
                response.append(v_split.point.segment.id)
                v_split.point.segment.reported = True
    else:
        if inside(v_split, x, x1, y, y1):
            if not v_split.point.segment.reported:
                response.append(v_split.point.segment.id)
                v_split.point.segment.reported = True
        v = v_split.left
        while not leaf(v):
            if x <= v.point.x:
                response += query1DRangeTree(v.tree_assoc, y, y1)
                v = v.left
            else:
                v = v.right
        if v and v.point.segment.reported:
            if inside(v, x, x1, y, y1):
                response.append(v.point.segment.id)
                v.point.segment.reported = True

        v = v_split.right
        while not leaf(v):
            if v.point.x <= x1:
                response += query1DRangeTree(v.tree_assoc, y, y1)
                v = v.right
            else:
                v = v.left
        if v and not v.point.segment.reported:
            if inside(v, x, x1, y, y1):
                response.append(v.point.segment.id)
                v.point.segment.reported = True
    return response