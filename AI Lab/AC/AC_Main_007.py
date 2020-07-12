from Generator_007 import *
from random import randint
import copy
import math
from util_007 import *
from AC1_007 import *
from AC2_007 import *
from AC3_007 import *
from AC4_007 import *



D = generateDomains()
N = 5

def assignDomains(nodes, D):

    for x in nodes:
        domain_number = randint(0, 5)
        x.domain = copy.copy(D[domain_number])
        #x.domain = [1, 2, 3, 4, 5]




def assignConstraints(nodes):
    constraints = {}
    c = 0
    for i in range(N):
        for j in range(i+1, N):
            if(i!=j):
                number_of_constraints = randint(0,1)
                if number_of_constraints!=0:
                    c += 1
                    if j not in nodes[i].neighbours:
                        nodes[i].neighbours.append(j)
                    if i not in nodes[j].neighbours:
                        nodes[j].neighbours.append(i)
                    lx1 = []
                    lx2 = []
                    for n in range(number_of_constraints):
                        cn = [0,2,4,5,6,7]
                        constraint_number = cn[randint(0,5)]
                        if constraint_number not in lx1:
                            lx1.append(constraint_number)
                    for a in lx1:
                        if(a==0):
                            lx2.append(1)
                        if(a==2):
                            lx2.append(3)
                        if(a==4):
                            lx2.append(4)
                        if(a==5):
                            lx2.append(5)
                        if(a==6):
                            lx2.append(6)
                        if(a==7):
                            lx2.append(8)
                    constraints[ (i,j) ] = lx1
                    constraints[ (j,i) ] = lx2
                    if c>=5:
                        return constraints
    return constraints


acx = []

ac1y = []
ac2y = []
ac3y = []
ac4y = []
f1 = open("ac1.txt", "w")
f2 = open("ac2.txt", "w")
f3 = open("ac3.txt", "w")
f4 = open("ac4.txt", "w")
p = 0
while p!=200:

    nodes = createNodes(N)
    assignDomains(nodes, D)
    cd = assignConstraints(nodes)

    n1 = copy.deepcopy(nodes)
    n2 = copy.deepcopy(nodes)
    n3 = copy.deepcopy(nodes)
    n4 = copy.deepcopy(nodes)
    c1 = copy.deepcopy(cd)
    c2 = copy.deepcopy(cd)
    c3 = copy.deepcopy(cd)
    c4 = copy.deepcopy(cd)

    r1,t1 = AC1(n1,c1)
    r2,t2 = AC2(n2,c2)
    r3,t3 = AC3(n3,c3)
    r4,t4 = AC4(n4,c4)

    if r1 and r2 and r3 and r4 == True:
        acx.append(N)

        ac1y.append(t1)
        ac2y.append(t2)
        ac3y.append(t3)
        ac4y.append(t4)
        f1.write(str(t1))
        f1.write("\n")
        f2.write(str(t2))
        f2.write("\n")
        f3.write(str(t3))
        f3.write("\n")
        f4.write(str(t4))
        f4.write("\n")
        p += 1
        print(p)
        plus = randint(0,1)
        N += plus

f1.close()
f2.close()
f3.close()
f4.close()


import matplotlib.pyplot as plt
plt.plot(acx, ac1y, label="AC-1")
plt.plot(acx, ac2y, label="AC-2")
plt.plot(acx, ac3y, label="AC-3")
plt.plot(acx, ac4y, label="AC-4")
plt.legend(loc="upper left")

plt.title("Performance graph", fontsize=16, fontweight='bold')
plt.xlabel("Number of nodes")
plt.ylabel("Time to finish successfully")
plt.show()
