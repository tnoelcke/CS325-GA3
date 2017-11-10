import sys  # Library for INT_MAX
 
 
# reference : http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
# in the works cited
class Graph():
 
    def __init__(self, vertices):
        weight = 0;
        self.V = vertices
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
 
        parent[0] = -1  # First node is always the root of
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)
 
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
                        parent[v] = u
 
        self.printMST(parent)
        self.weight = self.totalWeight(parent)
        return parent;
        
      
      
# where k=3 for the assignment!
def kthMST(G, k):
  # list of trees
  spanningTrees = [];
  # to hold E' (e prime)
  ePrime = []
  # use Pims alg to find MST for G
  mst = G.primMST()
  # add to list of trees
  spanningTrees.append(mst)
  #find tree with min weight
  mst = min(tree.weight for tree in spanningTrees)
  
  kMSTs[1] = mst
  
  for i in range(1,k):
    spanningTrees.remove(mst)
    # for each edge not in the min spanning tree
    # this can be done with list(set(G.graph) - set(mst)) I think
    for row in G.vertices:
      for col in G.vertices:
        if G.graph[row][col] not in mst:
          # Add E to MST // so there will generate a new cycle
          mst.append(G.graph[row][col])
          if i == 2:
            #  // For first MST we have to consider the equal edges too
            #  Select edges E’ from the cycle which have max weight and weight
            #  must be less than or equal to E
            for edge in mst:
              if edge <= G.graph[row][col] and max(mst):
                ePrime.append(edge)
          # Select edges E’ from the cycle which have max weight and weight
          # must be less than E
        else:
          for edge in mst:
            if edge < G.graph[row][col] and max(mst):
              ePrime.append(edge)
        mstPrime = []
          # for each edge in E' (e prime)
        for edge in ePrime:
          # MST’=Remove E’ from MST (can be done with sets i think)
          mstPrime = mst.remove(edge)
          # this step is maybe out of for loop
          spanningTrees.append(mstPrime)
    
    #find tree with min weight
    mst = min(tree.weight for tree in spanningTrees)
    # MST=List of trees.select min()
    # K MSTS[i]=MST
    kMSTs[i] = mst
    
  return kMSTs
                
                
          
  
  
  
  
  
  
 
g  = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
           ]
 
print(g.primMST());
print(g.graph)