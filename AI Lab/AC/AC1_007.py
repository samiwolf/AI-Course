from Generator_007 import *
from random import randint
import copy
import math
from util_007 import *
import time
def AC1(nodes, constraint_dictionary):
    start = time.time()
    rev = True
    while rev==True:
        rr = False
        for X in constraint_dictionary:
            xi = X[0]
            xj = X[1]
            constraints = constraint_dictionary[X]
            r, nodes = impose_constraints(nodes, xi,xj, constraints)
            if(nodes[xi].domain==[]):
                    return False, time.time() - start
            if(r==True):
                rr = True
        rev = rr
    end = time.time()
    return True, end-start
