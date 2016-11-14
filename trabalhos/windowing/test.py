# coding=UTF-8
import Windowing
from Windowing import *

x = []

#x.append(Point(6,6))
#x.append(Point(8,7))
#x.append(Point(10,4))
#x.append(Point(5,2))
#x.append(Point(3,5))

x.append(Point(0,0))
x.append(Point(2,4))
x.append(Point(1,0))
x.append(Point(4,2))

y = sorted(x, key=getKey)
print y

z = interval(y)
print z


#arv = RangeTree(x)
#arv = SegmentTree(x)
#r = queryWindow(arv)
#r = query2DRangeTree(arv, 2, 7, 2, 7)
#print r
#imprime_arv(arv)