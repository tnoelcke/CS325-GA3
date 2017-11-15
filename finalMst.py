import heapq
from heapq import heappush, heappop

#pretty prints the forest for debuging.
def displayForest(forest):
	for i in range(0, len(forest)):
		print(i, ": ", forest[i])


#sets up the heap 	
def setUpHeap(graph):
	heap = []
	for i in range(0, len(graph)):
		for j in range(0, i):
			heappush(heap, (int(graph[i][j]), i, j))
	return heap
	

#relabels all the verticies in a graph. This will be nessisary if we are changing a big
#label to a smaller one and if we are adding together two connected components
def reLabel(forest, newLabel, oldLabel):
	for i in range(0, len(forest)):
		if forest[i][0] == oldLabel:
			forest[i] = (newLabel, forest[i][1])


#Addes a new edge to the forests.
def addEdge(forest, edge1, edge2):
	forest[edge1][1].append(edge2)
	forest[edge2][1].append(edge1)


#finds the MST based on the heap passed to it along with the number of verticies.	
def findMst(heap, forest, V):
	weight = 0
	numEdge = 0
	#set up each node with a weight and a list to keep track of nodes.
	if len(forest) == 0:
		for i in  range(0, V):
			forest.append((-1,[])) #(Vertex name, Label, Ajecentcy list)
	while numEdge < V:
		safeEdge = heappop(heap)
		print(safeEdge)
		#if neither vertex has had any edges added to them.
		if forest[safeEdge[1]][0] < 0 and forest[safeEdge[2]][0] < 0:
			#we are adding another edge
			numEdge = numEdge + 1
			#label the connected component when it is created
			forest[safeEdge[1]] = (safeEdge[2], forest[safeEdge[1]][1])
			forest[safeEdge[2]] = (safeEdge[2], forest[safeEdge[2]][1])
			#add the edge to the ajacentcy list
			addEdge(forest, safeEdge[1], safeEdge[2])
			#add weight
			weight = weight + safeEdge[0]
		#if one of the vertex have has not yet had any edges added to it
		if forest[safeEdge[1]][0] < 0 or forest[safeEdge[2]][0] < 0:
			#we are adding another edge.
			numEdge = numEdge + 1
			addEdge(forest, safeEdge[1], safeEdge[2])
			weight = weight + safeEdge[0]
			#add lebel to edge, we are always using the smaller lebel which
			#the way we have implimented our heap will be the first label
			if forest[safeEdge[1]][0] < 0:
				forest[safeEdge[1]] = (safeEdge[2], forest[safeEdge[1]][1])
			#if a larger label is being changed to a smaller label we need go find that lebal
			#and ajust it every where it is used.
			else:
				#relabel the verticies
				reLabel(forest, safeEdge[2], safeEdge[1])
				#add the edge
				
				
		#if both of the edges are part of a connected componet make sure they are not the same connected component.
		if forest[safeEdge[1]][0] > 0 and forest[safeEdge[2]][0] > 0:
			#if they are not the same connected componenet connect them otherwise
			#don't add the edge because we will create a cycle.
			if forest[safeEdge[1]][0] != forest[safeEdge[2]][0]:
				#here we are adding another edge
				numEdge = numEdge + 1
				#relabel the edges
				reLabel(forest, safeEdge[2], safeEdge[1])
				#add the edge
				addEdge(forest, safeEdge[1], safeEdge[2])
				#add the weight
				weight = weight + safeEdge[0]
	print(weight)
			
			
	
graph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(graph[0][0])
del graph[0]

forest = []
heap = setUpHeap(graph)
findMst(heap, forest,totalVetices)
displayForest(forest)