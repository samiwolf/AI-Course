from Generator_007 import *
from random import randint
import copy
import math
import time
from util_007 import *
def AC3(nodes, constraint_dictionary):
    start = time.time()
    queue = Queue()
    for x in constraint_dictionary:
        queue.push(x)
    while not queue.isEmpty():
        X = queue.pop()
        xi = X[0]
        xj = X[1]
        constraints = constraint_dictionary[X]
        r, nodes = impose_constraints(nodes, xi,xj, constraints)
        if(r==True):
            if(nodes[xi].domain==[]):
                return False,  time.time() - start
            for a in nodes[xi].neighbours:
                if a!=xj:
                    ss = (a,xi)
                    queue.push(ss)
    end = time.time()
    return True, end-start
