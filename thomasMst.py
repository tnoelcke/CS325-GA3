import heapq
from heapq import heappush, heappop

def prims(graph, V):
  heap = []
  mst = []
  weight = 0
  test = []
  for i in range(0, len(graph)):
    test.append([])
    for j in range(0, i):
      if(graph[i][j] != 0):
        test[i].append(int(graph[i][j]))
        heappush(heap,(int(graph[i][j]), i, j))
  for i in range(0, len(test)):
    print(test[i])
  print(V)
  print(len(heap))
  while len(mst) < V:
    newEdge = heappop(heap)
    print(newEdge)
    if not(newEdge[1] in mst and newEdge[2] in mst):
      if not(newEdge[1] in mst):
        mst.append(newEdge[1])
      if not(newEdge[2] in mst):
        mst.append(newEdge[2])
      print(mst)
      print(len(mst))
      weight = weight + newEdge[0]
      print(weight)
  print (weight)

#graph = [[0, 1, 9, 9,1], [1, 0, 1, 9, 9], [9, 1, 0, 1, 9], [9, 9, 1, 0, 1], [1, 9, 9, 1, 0]]

fileGraph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVertices = int(fileGraph[0][0])
del fileGraph[0]
for i in range(0, len(fileGraph)):
  print(fileGraph[i])
prims(fileGraph, totalVertices)
  

  

