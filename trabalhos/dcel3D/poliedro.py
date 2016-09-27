#!/usr/bin/python
# coding=UTF-8
import Dcel
from Dcel import *

num_vert, num_faces = map(int,raw_input().split())
vertices = []
for i in xrange(num_vert):
    x,y,z = map(int,raw_input().split())
    vertices.append(Ponto(i+1,x,y,z))

faces = []
vertices_faces = []
for i in xrange(num_faces):
    v = map(int, raw_input().split())
    vertices_faces.append(v)
    faces.append(Face(i+1,None))

p = Poliedro(1, vertices, faces, vertices_faces)

if aberto(p):
    print 'aberto'
else:
    show_data(p, vertices_faces)
