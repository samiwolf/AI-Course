from random import randint
import copy
import math
from util_007 import *
import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def generateDomains():
    D = []
    d = []
    for i in range(21):
        d.append(i-20)
    D.append(d)

    d = []
    for i in range(1,21):
        d.append(i)
    D.append(d)

    d = []
    for i in range(2,21):
        if is_prime(i):
            d.append(i)
            d.append(-i)
    D.append(d)

    d = []
    for i in range(2,21, 2):
        d.append(i)
    D.append(d)

    d = []
    for i in range(1,21, 2):
        d.append(i)
    D.append(d)

    d = []
    for i in range(3,21):
        if i%3==0 or i%5==0:
            d.append(i)
            d.append(-i)
    D.append(d)
    return D

class Node(object):
    def __init__(self, n):
        self.id = n
        self.domain = []
        self.neighbours = []

def createNodes(n):
    nodes = []
    for i in range(n):
        temp = Node(i)
        nodes.append(temp)
    return nodes
