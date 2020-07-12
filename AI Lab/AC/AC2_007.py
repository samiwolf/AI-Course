from Generator_007 import *
from random import randint
import copy
import math
from util_007 import *
import time
def AC2(nodes, constraint_dictionary):
    start = time.time()
    rev = True
    for i in range(len(nodes)):
        q1 = Queue()
        q2 = Queue()
        for x in nodes[i].neighbours:
            q1.push((x,i))
            q2.push((i,x))
        while not q1.isEmpty():
            while not q1.isEmpty():
                X = q1.pop()
                xi = X[0]
                xj = X[1]
                constraints = constraint_dictionary[X]
                r, nodes = impose_constraints(nodes, xi,xj, constraints)
                if(nodes[xi].domain==[]):
                        return False, time.time() - start
                if r==True:
                    for a in nodes[xi].neighbours:
                        if  a!=xj:
                            ss = (a,xi)
                            q2.push(ss)
            q1 = q2
            q2 = Queue()
    end = time.time()
    return True, end-start
