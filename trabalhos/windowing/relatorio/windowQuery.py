#!/usr/bin/python
def windowQuery(segments, x, x1, y, y1):
    # define as fronteiras verticais
    window_left = Segment(-1, x, x, y, y1)
    window_right = Segment(-2, x1, x1, y, y1)
    # e as fronteiras horizontais
    window_top = Segment(-3, x, x1, y1, y1)
    window_bottom = Segment(-4, x, x1, y, y)

    # realiza a consulta e guarda em 'q1'
    q1 = query2DRangeTree(rtree, x, x1, y, y1)
    q2 = []
    # realiza uma consulta para cada fronteira da janela
    # e guarda em 'q2'
    querySegmentTreeVertical(stree_v, window_left, q2)
    querySegmentTreeVertical(stree_v, window_right, q2)
    querySegmentTreeHorizontal(stree_h, window_top, q2)
    querySegmentTreeHorizontal(stree_h, window_bottom, q2)

    return q1 + q2