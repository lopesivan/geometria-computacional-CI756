#!/usr/bin/python
# coding=UTF-8
import windowing
from windowing import *

segments = []
windows = []

n, w = map(int,raw_input().split())
for i in xrange(n):
    x, x1, y, y1 = map(int, raw_input().split())
    segments.append(Segment(i+1, x, x1, y, y1))

for i in xrange(w):
    x, x1, y, y1 = map(int, raw_input().split())
    resposta = windowQuery( segments, Window(x, x1, y, y1))
    print ' '.join( str(v) for v in resposta )
    clean(segments, resposta)
