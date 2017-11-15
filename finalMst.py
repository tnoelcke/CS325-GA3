import heapq
from heapq import heappush, heappop
import copy
from copy import deepcopy

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
def reLabel(forest, edge1, edge2):
	newLabel = 0
	oldLabel = 0
	if forest[edge1][0] > forest[edge2][0]:
		newLabel = forest[edge2][0]
		oldLabel = forest[edge1][0]
	else:  #forest[edge1][0] < forest[edge2][0]
		newLabel = forest[edge2][0]
		oldLabel = forest[edge1][0]
	for i in range(0, len(forest)):
		if forest[i][0] == oldLabel:
			forest[i] = (newLabel, forest[i][1])


#Addes a new edge to the forests.
def addEdge(forest, edge1, edge2):
	forest[edge1][1].append(edge2)
	forest[edge2][1].append(edge1)

#Removes an edege from the graph.
def removeEdge(graph, toRemove):
	try:
		graph[toRemove[1]][1].remove(toRemove[2])
		graph[toRemove[2]][1].remove(toRemove[1])
	except:
		pass

#finds the MST based on the heap passed to it along with the number of verticies.	
def findMst(heap, forest, edgesAdded, V):
	weight = 0
	numEdge = 0
	#set up each node with a weight and a list to keep track of nodes.
	if len(forest) == 0:
		for i in  range(0, V):
			forest.append((i,[])) #(Label, Ajecentcy list)
	while numEdge < V - 1:
		safeEdge = heappop(heap)
		print(safeEdge)
		print(numEdge)
		#if the two vertices aren't in the same component
		if forest[safeEdge[1]][0] != forest[safeEdge[2]][0]:
			print("SafeEdge Found")
			edgesAdded.append(safeEdge)
			#label the connected components
			reLabel(forest, safeEdge[1], safeEdge[2])
			#add the edge to the ajacentcy list
			addEdge(forest, safeEdge[1], safeEdge[2])
			#add weight
			weight = weight + safeEdge[0]
			numEdge = numEdge + 1
	return weight
	
#Lebels all the vertices in a component. Using DFS
def dfsLabel(graph, start, label):
	visited = []
	stack = [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.append(vertex)
			graph[vertex] = (label, graph[vertex][1])
			stack.extend(graph[vertex][1])
			

			

#given the mst in the forest along with a list of edges in the mst
#and the remaining edges in the heap left over from finding the mst
#this function finds the next mst.
def findNextMst(forest, edgesAdded, heap, weight):
	minWeight = 0
	edgeAdded = []
	tempWeight = 0
	heapState = []
	graphState = []
	for i in range(0, len(edgesAdded)):
		tempHeap = deepcopy(heap)
		tempEdge = edgesAdded[i]
		tempWeight = weight - tempEdge[0]
		removeEdge(forest, tempEdge)
		#We know there will only ever be two components we need to label so pick an edge
		#and preform the label the other edges should already all be labeled the same thing.
		#this will result in two unique componets.
		dfsLabel(forest, 0, i)
		tempEdgeAdded = []
		temp1 = findMst(tempHeap, forest, tempEdgeAdded, 2)
		print(temp1)
		temp = tempWeight + temp1
		print(temp)
		if minWeight == 0 or minWeight > temp:
			minWeight = temp
			edgeAdded = tempEdgeAdded
			heapState = deepcopy(tempHeap)
			graphState = deepcopy(forest)
		#set up for next iteration
		print(tempEdge)
		print(tempEdgeAdded)
		addEdge(forest, tempEdge[1], tempEdge[2])
		removeEdge(forest, tempEdgeAdded[0])
	print(minWeight)
	
	
	

graph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVetices = int(graph[0][0])
del graph[0]

forest = []
edgesAdded = []
weight = 0
heap = setUpHeap(graph)
weight = findMst(heap, forest, edgesAdded,totalVetices)
print("First: ", weight)
displayForest(forest)
findNextMst(forest, edgesAdded, heap, weight)



