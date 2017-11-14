#!/usr/bin/env python3

import heapq
from heapq import heappush, heappop, heapify
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
    heappush(memorization,MST1[0])

    #find MST2
    #small branch
    try:
        heap2S = deepcopy(heapMaster)
        heap2S.remove(heap2S[0])
        heap2SMaster = deepcopy(heap2S)
        MST2S = MSTNth(heap2S,V)
        print(MST2S)
        if MST2S[0] >= MST1[0]:
            heappush(memorization,MST2S[0])
    except:
        pass

    #big branch
    try:
        heap2B = deepcopy(heapMaster)
        heap2B.remove(MST1[1][0])
        heap2BMaster = deepcopy(heap2B)
        MST2B = MSTNth(heap2B, V)
        print(MST2B)
        if MST2B[0] >= MST1[0]:
            heappush(memorization,MST2B[0])
    except:
        pass

    #find MST3
    #travel down small branch
    try:
        heap3SS = deepcopy(heap2SMaster)
        heap3SS.remove(heap2S[0])
        MST3SS = MSTNth(heap3SS,V)
        print(MST3SS)
        if MST3SS[0] >= MST1[0]:
            heappush(memorization,MST3SS[0])
    except:
        pass
    
    try:
        heap3SB = deepcopy(heap2SMaster)
        heap3SB.remove(MST2S[1][0])
        MST3SB = MSTNth(heap3SB,V)
        print(MST3SB)
        if MST3SB[0] >= MST1[0]:
            heappush(memorization,MST3SB[0])
    except:
        pass

    #travel down big branch
    # try:
    #     heap3BS = deepcopy(heap2BMaster)
    #     heap3BS.remove(heap2B[0])
    #     MST3BS = MSTNth(heap3BS,V)
    #     print(MST3BS)
    #     if MST3BS[0] >= MST1[0]:
    #         heappush(memorization,MST3BS[0])
    # except:
    #      pass
    
    try:
        heap3BB = deepcopy(heap2BMaster)
        heap3BB.remove(MST2B[1][0])
        MST3BB = MSTNth(heap3BB,V)
        print(MST3BB)
        if MST3BB[0] >= MST1[0]:
            heappush(memorization,MST3BB[0])
    except:
        pass


    print(memorization)
    print(heappop(memorization))
    print(heappop(memorization))
    print(heappop(memorization))
    
#RUN PROG
fileGraph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(fileGraph[0][0])
del fileGraph[0]

findMSTs(fileGraph, totalVetices)
#END PROG