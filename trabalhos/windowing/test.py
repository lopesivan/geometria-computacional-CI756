# coding=UTF-8
import Windowing
from Windowing import *

x = []

x.append(Point(6,6))
x.append(Point(8,7))
x.append(Point(10,4))
x.append(Point(5,2))
x.append(Point(3,5))

y = sorted(x, key=getKey)

#arv = RangeTree(x)

#r = query2DRangeTree(arv, 2, 7, 2, 7)
#print r
#imprime_arv(arv)