# coding=UTF-8
import windowing
from windowing import *

x = []
segments = []
#segments.append(Segment(1, 1, 8, 8, 3))
#segments.append(Segment(2, 3, 5, 5, 2))
#segments.append(Segment(3, 6, 8, 6, 7))


segments.append(Segment(1, 2, 2, 4, 6))
segments.append(Segment(2, 1, 4, 7, 7))
segments.append(Segment(3, 1, 5, 8, 8))
segments.append(Segment(4, 2, 2, 9, 10))
segments.append(Segment(5, 3, 5, 10, 9))
segments.append(Segment(6, 1, 7, 14, 9))
segments.append(Segment(7, 6, 6, 11, 15))
segments.append(Segment(8, 5, 10, 7, 5))
segments.append(Segment(9, 7, 9, 12, 14))
segments.append(Segment(10, 9, 11, 12, 14))
segments.append(Segment(11, 8, 10, 7, 9))
segments.append(Segment(12, 12, 12, 3, 15))
segments.append(Segment(13, 13, 15, 9, 7))
segments.append(Segment(14, 3, 6, 2, 5))
segments.append(Segment(15, 7, 7, 2, 5))
segments.append(Segment(16, 13, 13, 2, 6))
segments.append(Segment(17, 2, 4, 14, 16))

#windows.append(Window(1, 6, 6, 7))
windows = []
#windows.append(Window(1, 3, 6, 10) ) #1
windows.append(Window(3, 13, 11, 15) ) #2 
#windows.append(Window(4, 8, 2, 4) ) #3
windows.append(Window(11, 14, 4, 5) ) #4
#windows.append(Window(11, 14, 6, 10) ) #5
#windows.append(Window(6, 7, 6, 11)) #6
for w in windows:
    resposta = windowQuery( segments, w )
    print ' '.join( str(v) for v in resposta )
    clean(segments, resposta)


#print r