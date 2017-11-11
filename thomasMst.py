import heapq
from heapq import heappush, heappop

def prims(graph, V):
  heap = []
  mst = []
  weight = 0
  for i in range(0, len(graph)):
    for j in range(i + 1, len(graph[i])):
      if(graph[i][j] != 0):
        heappush(heap, (graph[i][j], i, j))
  while len(mst) <= V:
    newEdge = heappop(heap)
    print(newEdge)
    print(mst)
    if not(newEdge[1] in mst and newEdge[2] in mst):
      mst.append(newEdge[1])
      mst.append(newEdge[2])
      weight = weight + newEdge[0]
  print (weight)
graph = [[0, 1, 9, 9,1], [1, 0, 1, 9, 9], [9, 1, 0, 1, 9], [9, 9, 1, 0, 1], [1, 9, 9, 1, 0]]  
prims(graph, len(graph) + 1)
  

  

