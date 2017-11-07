#codingutf-8
from math import *

#define angle
Acba = Acab = pi/180*80
Aacb = pi - Acba - Acab
Acbe = pi/180*30
Acaf = pi/180*20
Aabe = Acba - Acbe
Aaeb = pi - Acab - (Aabe)

#define segment
ab = ae = 2
ac = bc = (ab/2)/cos(Acab)
eo = (ac/2)-ae
fo = (ac/2)*sin(Acaf)
Aefo = atan(eo/fo)
Aefa = pi - Acaf - pi/2 - Aefo
x = Aefa/(pi/180)
print(x)
