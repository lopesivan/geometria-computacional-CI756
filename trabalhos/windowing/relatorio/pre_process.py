def pre_process(segments):
    endpoints = []
    for s in segments:
        endpoints.append(s.upper)
        endpoints.append(s.lower)

    sorted_endpoints_x = sorted(endpoints, key=getKeyX)
    sorted_endpoints_y = sorted(endpoints, key=getKeyY)

    # constroi a Range Tree
    rtree = RangeTree(sorted_endpoints_x)


    # constroi os intervalos elementares com base na 
    # coordenada x
    elem_intervals_v = interval_x(sorted_endpoints_x)
    # e com base na coordenada y,
    elem_intervals_h = interval_y(sorted_endpoints_y)

    # constroi a arvore de segmentos vertical 
    stree_v = segmentTreeX(elem_intervals_v, segments)
    # e horizontal
    stree_h = segmentTreeY(elem_intervals_h, segments)

    return rtree, stree_v, stree_h