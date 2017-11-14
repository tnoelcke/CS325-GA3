import heapq
from heapq import heappush, heappop


def setUpHeap(graph):
	heap = []
	for i in range(0, len(graph)):
		for j in range(0, i):
			heappush(heap, int(graph[i][j]), i, j)
	return heap
	
def findMst(heap, V):
	forest = []
	weight = 0
	heap = []
	numEdge = 0
	#set up each node with a weight and a list to keep track of nodes.
	for i in  range(0, V):
		forest.append((-1,[]) #(Vertex name, Label, Ajecentcy list)
	while numEdge < V:
		safeEdge = heappop(heap)
		#if neither vertex has had any edges added to them.
		if forest[safeEdge[1]][0] < 0 and forest[safeEdge[2]][0] < 0:
			numEdge = numEdge + 1
		#if one of the vertex have has not yet had any edges added to it
		if forest[safeEdge[1]][0] < 0 or forest[safeEdge[2]][0] < 0:
			numEdge = numEdge + 1
		#if both of the edges are part of a connected componet make sure they are not the same connected component.
		if forest[safeEdge[1]][0] > 0 and forest[safeEdge[2]][0] > 0:
			#if they are not the same connected componenet connect them otherwise
			#don't add the edge because we will create a cycle.
			if forest[safeEdge[1]][0] != forest[safeEdge[2]][0]:
				numEdge = numEdge + 1
			
			
	
graph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(fileGraph[0][0])
del graph[0]

heap = setUpHeap(graph)
print(heap)
findMst(heap)