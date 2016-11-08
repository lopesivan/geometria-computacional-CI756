# coding=UTF-8
import Windowing
from Windowing import *

x = []

x.append(Point(10,10))
x.append(Point(20,20))
x.append(Point(30,20))
x.append(Point(5,20))
x.append(Point(3,20))
x.append(Point(50,20))
x.append(Point(40,20))
x.append(Point(70,20))
x.append(Point(60,20))
x.append(Point(90,20))

#arv = ArvBinBusca(x, 1)

root = None
for p in x:
    root = insert(root, p)

imprime_arv(root)