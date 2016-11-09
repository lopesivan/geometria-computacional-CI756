# coding=UTF-8
import Windowing
from Windowing import *

x = []

x.append(Point(6,6))
x.append(Point(8,7))
x.append(Point(10,4))
x.append(Point(5,2))
x.append(Point(3,5))


arv = RangeTree(x)

r = query2DRangeTree(arv, 5, 9, 5, 9)
print r
#imprime_arv(arv)