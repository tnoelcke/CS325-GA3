#!/usr/bin/env python3

import heapq
from heapq import heappush, heappop
import copy
from copy import deepcopy







def MSTNth(heap, V):
    #find MST based on input variable. Exiled Edges will cause us to find the nth MST where n is the
    #number of exiled edges.
    weight = 0
    S = []
    ExiledEdges = []
    for i in range(0, len(heap)):
        safeEdge = heappop(heap)
        if not(safeEdge[1] in S and safeEdge[2] in S):
            if(safeEdge[1] not in S): S.append(safeEdge[1])
            if(safeEdge[2] not in S): S.append(safeEdge[2])
            weight = weight + safeEdge[0]
            if len(S) == (V):
                ExiledEdges.append(safeEdge) #push largest edge onto Exiled Edges
                break
    return (weight, ExiledEdges)

def buildHeap(graph):
    heap = []
    # load up the values. We will replace reading the graph with file IO later.
    for i in range(0, len(graph)):
        for j in range(i + 1, len(graph[i])):
            heappush(heap, (int(graph[i][j]), int(i), int(j)))
    #print(heap)
    return heap

def findMSTs(graph, V):
    
    heapMaster = buildHeap(graph)
    memorization = []

    #find MST1
    heap1 = deepcopy(heapMaster)
    MST1 = MSTNth(heap1, V)
    memorization.heappush(MST1[0])

    #find MST2
    heap2S = deepcopy(heapMaster)
    
    heap2S.remove(heap2S[0])
    heap2SMaster = deepcopy(heap2S)
    MST2S = MSTNth(heap2S,V)

    heap2B = deepcopy(heapMaster)
    heap2B.remove(MST1[1][0])
    heap2BMaster = deepcopy(heap2B)
    MST2B = MSTNth(heap2B, V)

    if(MST2S[0] < MST2B[0]):
        MST2 = MST2S
        heap2Master = heap2SMaster
    else:
        MST2 = MST2B
        heap2Master = heap2BMaster

    #find MST3
    heap3S = deepcopy(heap2Master)
    heap3S.remove(heap3S[0])
    MST3S = MSTNth(heap3S,V)

    heap3B = deepcopy(heap2Master)
    heap3B.remove(MST2[1][0])
    MST3B = MSTNth(heap3B,V)

    if(MST3S[0] < MST3B[0]):
        MST3 = MST3S
    else:
        MST3 = MST3B
    

    print(MST1)
    print(MST2)
    print(MST3)
  
  

#RUN PROG
fileGraph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(fileGraph[0][0])
del fileGraph[0]

findMSTs(fileGraph, totalVetices)
#END PROG