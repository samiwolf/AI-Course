from Generator_007 import *
from random import randint
import time
import copy
import math
from util_007 import *
def getSupport(nodes, constraint_dictionary):
    S = {}
    for i in range(len(nodes)):
        #print(nodes[i].neighbours)
        for d in nodes[i].domain:
            cnt = 0
            l = []
            for j in nodes[i].neighbours:
                for dd in nodes[j].domain:
                    con_list = constraint_dictionary[(i,j)]
                    for constraint in con_list:
                        if constraint==0:
                            if d>=dd:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==1:
                            if d<dd:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==2:
                            if d<=dd:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==3:
                            if d>dd:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==4:
                            if d==dd:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==5:
                            if d!=dd:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==6:
                            if d==(-1*dd):
                                cnt += 1
                                l.append((j,dd))
                        if constraint==7:
                            if d==dd**2:
                                cnt += 1
                                l.append((j,dd))
                        if constraint==8:
                            if dd==d**2:
                                cnt += 1
                                l.append((j,dd))

            S[(i,d)] = l
    return S
def getCounter(nodes,S):
    Counter = {}
    for p in S:
        l = S[p]
        cnt = {}
        for i in range(len(nodes)):
            cnt[i] = 0
        for t in l:
            if cnt[t[0]] == 0:
                cnt[t[0]] = 1
            else:
                cnt[t[0]] += 1
        for c in cnt:
            if c!= p[0] and nodes[p[0]].neighbours.count(c)>0:
                Counter[(p[0], p[1], c)] =  cnt[c]
    return Counter
def AC4(nodes, constraint_dictionary):
    start = time.time()
    S = getSupport(nodes, constraint_dictionary)
    Counter = getCounter(nodes, S)
    l = []
    for x in Counter:
        if(Counter[x]==0):
            us = (x[0], x[1])
            if us not in l:
                l.append(us)
    rq = Queue()
    while l:
        X = l.pop()
        rq.push(X)
        for supporter in S[X]:
            temp = (supporter[0], supporter[1], X[0])
            Counter[temp] -= 1
            if(Counter[temp]==0):
                l.append(supporter)
    while not rq.isEmpty():
        X = rq.pop()
#        print(X)
        if nodes[X[0]].domain == []:
            return False
        if nodes[X[0]].domain.count(X[1]) > 0:
                nodes[X[0]].domain.remove(X[1])
                if nodes[X[0]].domain == []:
                    return False, time.time() - start
    end = time.time()
    return True, end -  start
