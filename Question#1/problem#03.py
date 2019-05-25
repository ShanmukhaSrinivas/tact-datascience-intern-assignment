#This program shows the diffrence b/w normal python program and numba

import quantecon as qe
from numba import jit
from array import *
def l():
    arr = array('i',[10,11,12,13,14])
    arr[1] = 80
    for x in arr:
        print(x)

@jit
def k():
    arr = array('i',[10,11,12,13,14])
    arr[1] = 80
    for x in arr:
        print(x)

qe.util.tic()
l()
p1 = qe.util.toc()
qe.util.tic()
k()
p2 = qe.util.toc()
print(p1/p2)