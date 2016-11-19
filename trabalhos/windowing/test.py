# coding=UTF-8
import windowing
from windowing import *

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
resposta = windowQuery( segments, Window(4, 7, 5, 7) )
print resposta
#print r