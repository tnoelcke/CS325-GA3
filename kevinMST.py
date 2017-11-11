#!/usr/bin/env python3
from heapq import heappush, heappop

heap = []
totalEdges = 0
totalVetices = 0

#fileIO
lines = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(lines[0][0])
del lines[0]

#fill heap
for x in range(0,totalVetices):
    for y in range(x+1,totalVetices):
        heappush(heap,(int(lines[x][y]),int(x),int(y)))
        totalEdges += 1

# print(totalVetices)
# print(totalEdges)

#intialize weights for each min span tree
visitedNum = 0
visited = [False for i in range(0,totalVetices)]
totalWeightOne = 0
totalWeightTwo = 0
totalWeightThree = 0


#find weight of most min spann tree
for i in range(0,totalEdges):
    item = heappop(heap)
    weight = item[0]
    x = item[1]
    y = item[2]
    xflag = False
    yflag = False
    #print(weight,x,y)
    if(visited[x] == False or visited[y] == False):
        #print(weight)
        totalWeightOne += weight
        if(visited[x] == False):
            xflag = True
            visited[x] = True
            visitedNum += 1
        if(visited[y] == False):
            yflag = True
            visited[y] = True
            visitedNum += 1
    if(visitedNum == totalVetices):
        totalWeightTwo = totalWeightOne - weight
        if xflag:
            visited[x] = False
            visitedNum -= 1
        if yflag:
            visited[y] = False
            visitedNum -= 1
        break

for j in range(i,totalEdges):
    item = heappop(heap)
    weight = item[0]
    x = item[1]
    y = item[2]
    xflag = False
    yflag = False
    #print(weight,x,y)
    if(visited[x] == False or visited[y] == False):
        #print(weight)
        totalWeightTwo += weight
        if(visited[x] == False):
            xflag = True
            visited[x] = True
            visitedNum += 1
        if(visited[y] == False):
            yflag = True
            visited[y] = True
            visitedNum += 1
    if(visitedNum == totalVetices):
        totalWeightThree = totalWeightTwo - weight
        if xflag:
            visited[x] = False
            visitedNum -= 1
        if yflag:
            visited[y] = False
            visitedNum -= 1
        break

for k in range(j,totalEdges):
    item = heappop(heap)
    weight = item[0]
    x = item[1]
    y = item[2]
    xflag = False
    yflag = False
    #print(weight,x,y)
    if(visited[x] == False or visited[y] == False):
        #print(weight)
        totalWeightThree += weight
        if(visited[x] == False):
            visited[x] = True
            visitedNum += 1
        if(visited[y] == False):
            visited[y] = True
            visitedNum += 1
    if(visitedNum == totalVetices):
        break

print(totalWeightOne)
print(totalWeightTwo)
print(totalWeightThree)