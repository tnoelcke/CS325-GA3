import sys  # Library for INT_MAX
import operator
 
# reference : http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
# in the works cited
class Graph():
 
    def __init__(self, vertices):
        weight = 0;
        self.V = vertices
        self.weight = 0
        self.keys = [sys.maxsize] * self.V
        self.cols = [sys.maxsize] * self.V
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
 
    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
 
    # A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):
 
        # Initilaize min value
        min = sys.maxsize
 
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index

    def printGraph(self):
        print("MST:",self.graph,"Keys:",self.keys,"weight:",self.weight)

    def calcWeight(self):
        for j in range(self.V):
                for k in range(self.V):
                    if self.graph[j][k] == self.graph[k][j]:
                        self.weight += self.graph[j][k]
    
    
    def totalWeight(self,parent):
        print("Edge \tWeight")
        total = 0
        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
            total += self.graph[i][ parent[i] ]
        print("total weight: ", total)
        return total
 
    # Function to construct and print MST for a graph represented using
    # adjacency matrix representation
    def primMST(self):
 
        #Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        key[0] = 0   # Make key 0 so that this vertex is picked as first vertex
        mstSet = [False] * self.V
        mstGraph = Graph(self.V)
 
        parent[0] = -1  # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
            print("min vertex index",u)
            print("key weight:,",key)
            print("MSTset",mstSet)
            print("parent",parent)
            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True
 
            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        print("weights to add:",self.graph[u][v])
                        print("add to MST",u)
                        parent[v] = u

        for i in range(1,self.V):
            print(parent[i],"-",i,"\t",self.graph[i][ parent[i] ])
            mstGraph.graph[i][parent[i]] = self.graph[i][ parent[i] ]
            mstGraph.graph[parent[i]][i] = self.graph[i][ parent[i] ]
        
        self.printMST(parent)
        self.weight = self.totalWeight(parent)
        mstGraph.weight = self.weight
        return mstGraph;
        
      
      
# where k=3 for the assignment!
def kthMST(G, k):
  kMSTs = [Graph(G.V) for i in range(G.V)]
  tempMST = Graph(G.V)
  # list of trees
  spanningTrees = [];
  # to hold E' (e prime)
  ePrime = Graph(G.V)
  ePrimeVals = [None] * G.V
  # use Pims alg to find MST for G
  mst = Graph(G.V)
  mst = G.primMST()
  print("MST : ",mst.graph)
  
  # add to list of trees
  spanningTrees.append(mst)
  #find tree with min weight
  minWeight = min(tree.weight for tree in spanningTrees)
  mst = next(tree for tree in spanningTrees if tree.weight == minWeight)
  print(mst.graph)
  kMSTs[0] = mst.weight
  count = 0;
  for i in range(1,k):
    
    print(count)
    spanningTrees.remove(mst)
    # for each edge not in the min spanning tree
    # this can be done with list(set(G.graph) - set(mst)) I think
    print("keys", mst.keys)
    for row in range(G.V):
      for col in range(G.V):
        if(col > len(mst.graph)):
            print("index err")
        if G.graph[row][col] != mst.graph[row][col] and G.graph[col][row] != mst.graph[col][row] and G.graph[row][col] > 0:
          count += 1
          print(count)
          print("row, col, w:" ,row, col, G.graph[row][col] )
          print(mst.graph , "\n\n")
          # Add E to MST // so there will generate a new cycle
          mst.graph[row][col] = G.graph[row][col]
          mst.graph[col][row] = G.graph[col][row]
          # too keep track of vertices not in OG mst
          mst.cols[row] = col
          mst.keys.append(G.graph[row][col])
          #print("keys", mst.keys)
          if i == 1:
            #  // For first MST we have to consider the equal edges too
            #  Select edges E’ from the cycle which have max weight and weight
            #  must be less than or equal to E
            for j in range(G.V):
                for k in range(G.V):
                  #print(edge)
                  if mst.graph[j][k] <= G.graph[j][k] and mst.graph[k][j] <= G.graph[k][j]:
                    ePrime.graph[j][k] = G.graph[j][k]
                    ePrime.graph[k][j] = G.graph[k][j]
            print("E' : ",ePrime.graph)
            print("mst: ",mst.graph)
          # Select edges E’ from the cycle which have max weight and weight
          # must be less than E
          else:
              for j in range(G.V):
                for k in range(G.V):
                  #print(edge)
                  if mst.graph[j][k] < G.graph[j][k] and mst.graph[k][j] < G.graph[k][j]:
                    ePrime.graph[j][k] = G.graph[j][k]
                    ePrime.graph[k][j] = G.graph[k][j]

                    
          mstPrime = Graph(G.V)
          mstTemp = []
          mstTempkey = []
          # for each edge in E' (e prime)
          #print(len(ePrime))
          
          for j in range(G.V):
             #MST’=Remove E’ from MST (can be done with sets i think)
            for j in range(G.V):
                for k in range(G.V):
                  #print(edge)
                  if ePrime.graph[j][k] == mst.graph[j][k] and ePrime.graph[k][j] == mst.graph[k][j]:
                    mst.graph[j][k] = 0
                    mst.graph[k][j] = 0
                    spanningTrees.append(mst)                    
        
    #find tree with min weight
    for tree in spanningTrees:
        tree.calcWeight()
    minWeight = min(tree.weight for tree in spanningTrees)
    mst = next(tree for tree in spanningTrees if tree.weight == minWeight)       
    
    # MST=List of trees.select min()
    # K MSTS[i]=MST
    kMSTs[i] = mst.weight
  print(spanningTrees[0].weight,spanningTrees[1].weight,spanningTrees[2].weight)
  return spanningTrees[0:2]
                
                
          
  
  
  
  
  
  
graph = [line.rstrip('\n').split(',') for line in open('input.txt','r')]
totalVertices = int(graph[0][0])
del graph[0]
#parses graph as an int array
for i in range(0, len(graph)):
    for j in range(0, len(graph[i])):
        graph[i][j] = int(graph[i][j])

g  = Graph(totalVertices)
g.graph = graph
 
#print(g.primMST());
#print(g.graph)
print(kthMST(g,3))
