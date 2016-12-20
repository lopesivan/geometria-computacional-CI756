#!/usr/bin/python
# coding=UTF-8
import Windowing
from Windowing import *

segments = []
windows = []

n, w = map(int,raw_input().split())
for i in xrange(n):
    x, x1, y, y1 = map(int, raw_input().split())
    segments.append(Segment(i+1, x, x1, y, y1))

rtree, stree_v, stree_h, blou = pre_process(segments)

for i in xrange(w):
    x, x1, y, y1 = map(int, raw_input().split())
    resposta = windowQuery( Window(x, x1, y, y1), rtree, blou, blou.tree_assoc )
    print ' '.join( str(v) for v in resposta )
    clean(segments, resposta)
