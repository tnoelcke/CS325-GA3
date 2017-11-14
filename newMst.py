import heapq
from heapq import heappush, heappop



def prims(graph):
	Tree = []
	heap = []
	weight = 0
	wieghtArray = []
	#keeps track of what vertex we are currently on
	index = 0
	Tree.append(index)
	lastWeight = 0
	while(len(Tree) < len(graph)):
		for i in range(0, len(graph)):
			if int(graph[index][i]) > 0:
				heappush(heap, (int(graph[index][i]), index, i))
		added = False
		while not added:
			safeEdge = heappop(heap)				
			if safeEdge[2] not in Tree:
				Tree.append(safeEdge[2])
				weight = weight + safeEdge[0]
				index = safeEdge[2]
				added = True
				lastWeight = safeEdge[0]
	print(weight)

	
	
graph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVertices = int(graph[0][0])
del graph[0]
prims(graph)





