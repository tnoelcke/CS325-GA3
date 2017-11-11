#!/usr/bin/env python3

import heapq
from heapq import heappush, heappop

heap = []



def MSTNth(heap, S, ExiledEdges, V, weight):
    #find MST based on input variable. Exiled Edges will cause us to find the nth MST where n is the
    #number of exiled edges.

    for i in range(0, len(heap)):
        safeEdge = heappop(heap)



        if not(safeEdge[1] in S and safeEdge[2] in S) and (safeEdge not in ExiledEdges):
            S.append(safeEdge[1])
            S.append(safeEdge[2])
            weight = weight + safeEdge[0]
        if len(S) == (V - 1):
            ExiledEdges.append(safeEdge)
            S.remove(safeEdge[1])
            S.remove(safeEdge[2])
            #this looks weird but it allows me to pass the actual weight for the MST and the
            #weight minus the last edge. This will come in handy later.
            break
    print(S)
    return (weight, weight - safeEdge[0])
      


def findMST(graph, V):
    # load up the values. We will replace reading the graph with file IO later.
    for i in range(0, len(graph)):
        for j in range(i + 1, len(graph[i])):
            heappush(heap, (int(graph[i][j]), int(i), int(j)))

    #print(heap)

    S1 = []
    S2 = []
    S3 = []
  
    exiledEdges = []
    totalWeight1 = 0
    totalWeight2 = 0
    totalWeight3 = 0

    #find MST1
    print(MSTNth(heap, S1, exiledEdges, V, totalWeight1) )
#   print("weight: ",totalWeight1)
#   print(S1)
#   #find MST2
#   S2.append(S1)
#   (totalWeight2, totalWeight3) = MSTNth(heap, S2, exiledEdges, V, totalWeight2)
#   print(totalWeight2)
#   S3.append(S3)
#   (totalWeight3, temp) = MSTNth(heap, exiledEdges, V, exiledEdges, totalWeight3)
#   print(totalWeight3)
  
  
  #findMST3
  
  
  
#graph = [[ 1, 2, 3], [4, 5], [6], []]

fileGraph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(fileGraph[0][0])
del fileGraph[0]

findMST(fileGraph, totalVetices)