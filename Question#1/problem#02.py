from numba import njit
import time
import quantecon as qe
@njit
def nor_py(a1,a2):
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]
    dz = a2[2] - a1[2]
    r = (dx*dx+dy*dy+dz*dz)**0.5
    return r

def num_py(a1,a2):
    dx = a2[0] - a1[0]
    dy = a2[1] - a1[1]
    dz = a2[2] - a1[2]
    r = (dx*dx+dy*dy+dz*dz)**0.5
    return r

a1 = [11,13,15]
a2 = [10,12,14]
qe.util.tic()
num_py(a1,a2)
p1 = qe.util.toc()
qe.util.tic()
nor_py(a1,a2)
p2 = qe.util.toc()
print(p1,p2)