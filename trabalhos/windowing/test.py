# coding=UTF-8
import Windowing
from Windowing import *

x = []
segments = []
segments.append(Segment(1, 1, 8, 8, 3))
segments.append(Segment(2, 3, 5, 5, 2))
segments.append(Segment(3, 6, 8, 6, 7))

#segments.append(Point(6,6))
#x.append(Point(8,7))
#x.append(Point(10,4))
#x.append(Point(5,2))
#x.append(Point(3,5))

#x.append(Point(0,0))
#x.append(Point(2,4))
#x.append(Point(1,0))
#x.append(Point(4,2))
for s in segments:
    x.append(s.upper)
    x.append(s.lower)


y = sorted(x, key=getKey)
print y

z = interval(y)
print z


arv = RangeTree(y)
#arv = SegmentTree(z)
#r = queryWindow(arv)
#r = query2DRangeTree(arv, 4, 7, 5, 7)
r = query2DRangeTree(arv, 1, 6, 1, 6)
#imprime_intervalos(arv)
imprime_arv(arv)
print r