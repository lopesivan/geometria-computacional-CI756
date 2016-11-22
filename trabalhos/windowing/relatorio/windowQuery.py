#!/usr/bin/python
def windowQuery(segments, x, x1, y, y1):
    endpoints = []
    for s in segments:
        endpoints.append(s.upper)
        endpoints.append(s.lower)

    sorted_endpoints_x = sorted(endpoints, key=getKeyX)
    sorted_endpoints_y = sorted(endpoints, key=getKeyY)

    # constroi a Range Tree
    rtree = RangeTree(sorted_endpoints_x)
    # realiza a consulta e guarda em 'q1'
    q1 = query2DRangeTree(rtree, x, x1, y, y1)

    # constroi os intervalos elementares com base na 
    # coordenada x
    elem_intervals_v = interval_x(sorted_endpoints_x)
    # e com base na coordenada y,
    elem_intervals_h = interval_y(sorted_endpoints_y)

    # constroi a arvore de segmentos vertical 
    stree_v = segmentTreeX(elem_intervals_v, segments)
    # e horizontal
    stree_h = segmentTreeY(elem_intervals_h, segments)

    # define as fronteiras verticais
    window_left = Segment(-1, x, x, y, y1)
    window_right = Segment(-2, x1, x1, y, y1)
    # e as fronteiras horizontais
    window_top = Segment(-3, x, x1, y1, y1)
    window_bottom = Segment(-4, x, x1, y, y)

    q2 = []

    # realiza uma consulta para cada fronteira da janela
    # e guarda em 'q2'
    querySegmentTreeVertical(stree_v, window_left, q2)
    querySegmentTreeVertical(stree_v, window_right, q2)
    querySegmentTreeHorizontal(stree_h, window_top, q2)
    querySegmentTreeHorizontal(stree_h, window_bottom, q2)

    return q1 + q2