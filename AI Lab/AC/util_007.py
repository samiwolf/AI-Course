from Generator_007 import *
from random import randint
import copy
import math
from util_007 import *

class Queue:
    def __init__(self):
        self.list = []

    def push(self,item):
        self.list.insert(0,item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0


def impose_constraints(nodes, xi, xj, constraints):
    revised = False
    for c in constraints:
        if c==0:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x>=y and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
        if c==1:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x<y and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
        if c==2:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x<=y and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
        if c==3:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x>y and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
        if c==4:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x==y and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
        if c==5:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x!=y and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)

        if c==6:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x== (-1*y) and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)

        if c==7:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if x==y**2 and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
        if c==8:
            temp = []
            for x in nodes[xi].domain:
                for y in nodes[xj].domain:
                    if y==x**2 and x not in temp:
                        temp.append(x)
            if(nodes[xi].domain!=temp):
                revised = True
                nodes[xi].domain = copy.copy(temp)
    return revised, nodes
