from random import randint
import numpy as np

step = 0

def getNQueensGrid(N):
    return np.array(np.zeros(shape = (N,N), dtype=int))

def randomAssignment(grid):
    for i in range(len(grid)):
        j = randint(0, len(grid)-1)
        grid[j,i] = 1
    return grid


def solveNQueensLocalSearch(grid, position):
    global step
    step += 1
    print(grid)
    print("Current column - " + str(position))
    if len(grid) == position:
        return True
    rowsProposition = getRows(grid, position)
    for row in rowsProposition:
            grid[row[0], position] = 1
            if solveNQueensLocalSearch(grid, position + 1):
                return True
            grid[row[0], position] = 0
    return False


def countPositionConflict(grid, row, column):
    c = 0
    list = []
    for col in range(len(grid)):
        if grid[row, col] == 1 and col != column:
            c += 1
            list.append((row,col))
            break;
    for col in range(column-1, -1, -1):
        if grid[row, col] == 1 and col != column:
            c += 1
            list.append((row,col))
            break;

    for ro in range(len(grid)):
        if grid[ro, column] == 1 and ro != row:
            c += 1
            list.append((ro,column))
            break;
    for ro in range(row-1, -1, -1):
        if grid[ro, column] == 1 and ro != row:
            c += 1
            list.append((ro,column))
            break;
    iR = row
    iC = column
    while iC >= 0 and iR >= 0:
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            c += 1
            list.append((iR,iC))
            break;
        iC -= 1
        iR -= 1
    iR = row
    iC = column
    while iC >= 0 and iR < len(grid):
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            c += 1
            list.append((iR,iC))
            break;
        iR += 1
        iC -= 1
    iR = row
    iC = column
    while iC < len(grid) and iR < len(grid):
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            c += 1
            list.append((iR,iC))
            break;
        iR += 1
        iC += 1
    iR = row
    iC = column
    while iC < len(grid) and iR >=0:
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            c += 1
            list.append((iR,iC))
            break;
        iR -= 1
        iC += 1
    return c, list

def getRows(grid, position):
    for row in range(len(grid)):
        grid[row,position] = 0
    rows = []
    for row in range(len(grid)):
            cc, rr = countPositionConflict(grid, row, position)
            rows.append( (row, cc, rr) )
    rows.sort(key=lambda tup: tup[1])
    #print(rows)
    return rows

def isSafe(grid, row, column):
    iR = row
    iC = column
    while iC >= 0 and iR >= 0:
        if grid[iR, iC] == 1  and iR != row and iC !=column:
            return False
        iC -= 1
        iR -= 1

    iR = row
    iC = column
    while iC >= 0 and iR < len(grid):
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            return False
        iR += 1
        iC -= 1
    iR = row
    iC = column
    while iC < len(grid) and iR < len(grid):
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            return False
        iR += 1
        iC += 1
    iR = row
    iC = column
    while iC < len(grid) and iR >= 0:
        if grid[iR, iC] == 1 and iR != row and iC !=column:
            return False
        iR -= 1
        iC += 1


    for col in range(len(grid)):
        if grid[row, col] == 1:
            return False
    for col in range(column-1, -1, -1):
        if grid[row, col] == 1:
            return false
    for ro in range(len(grid)):
        if grid[ro, column] == 1:
            return False
    for ro in range(row-1, -1, -1):
        if grid[ro, column] == 1:
            return false
    return True

def isSolved(grid):
    c = 0
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row,col] == 1 :
                    grid[row, col] = 0
                    if isSafe(grid,row,col):
                        c += 1
                    grid[row, col] = 1
    if c==len(grid):

        return True
    return False


import time
import copy


start = time.time()
grd = None
while True:
    gr = getNQueensGrid(8)
    gr = randomAssignment(gr)
    grd = copy.copy(gr)
    solveNQueensLocalSearch(gr, 0)
    if isSolved(gr):
        break
end = time.time()
print("Initial 8x8 Grid")
print(grd)
print("Final Grid")
print(gr)
print("Total Step - " + str(step))
print("Time - " + str(end-start))
print("\n\n")

start = time.time()
grd = None
while True:
    gr = getNQueensGrid(10)
    gr = randomAssignment(gr)
    grd = copy.copy(gr)
    solveNQueensLocalSearch(gr, 0)
    if isSolved(gr):
        break
end = time.time()
print("Initial 10x10 Grid")
print(grd)
print("Final Grid")
print(gr)
print("Total Step - " + str(step))
print("Time - " + str(end-start))
print("\n\n")

start = time.time()
grd = None
while True:
    gr = getNQueensGrid(15)
    gr = randomAssignment(gr)
    grd = copy.copy(gr)
    solveNQueensLocalSearch(gr, 0)
    if isSolved(gr):
        break
end = time.time()
print("Initial 15x15 Grid")
print(grd)
print("Final Grid")
print(gr)
print("Total Step - " + str(step))
print("Time - " + str(end-start))
print("\n\n")

start = time.time()
grd = None
while True:
    gr = getNQueensGrid(20)
    gr = randomAssignment(gr)
    grd = copy.copy(gr)
    solveNQueensLocalSearch(gr, 0)
    if isSolved(gr):
        break
end = time.time()
print("Initial 20x20 Grid")
print(grd)
print("Final Grid")
print(gr)
print("Total Step - " + str(step))
print("Time - " + str(end-start))
