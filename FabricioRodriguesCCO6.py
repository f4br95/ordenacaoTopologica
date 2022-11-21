#Creditos: Neelam Yadav

'''
Aluno: Fabrício de Paulo Rodrigues
Turma: Ciencia da Computação, 6o periodo 

'''






from collections import defaultdict
n_vertices = 7
# Class represent Graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency List
        self.adj = defaultdict(list)
        self.NumVertices = vertices # No. of vertices
        self.cost = [0,0,0,0,0,0,0] 
        self.cam_max = [0,0,0,0,0,0,0] 
        self.ordely = [] 
        self.V = vertices

 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # The function to do Topological Sort.
    def topologicalSort(self):
         
        # Create a vector to store indegrees of all
        # vertices. Initialize all indegrees as 0.
        in_degree = [0]*(self.NumVertices)
         
        # Traverse adjacency lists to fill indegrees of
           # vertices.  This step takes O(V + E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1
 
        # Create an queue and enqueue all vertices with
        # indegree 0
        queue = []
        for i in range(self.NumVertices):
            if in_degree[i] == 0:
                queue.append(i)
 
        # Initialize count of visited vertices
        cnt = 0
 
        # Create a vector to store result (A topological
        # ordering of the vertices)
        top_order = []
 
        # One by one dequeue vertices from queue and enqueue
        # adjacents if indegree of adjacent becomes 0
        while queue:
 
            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = queue.pop(0)
            top_order.append(u)
 
            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)
 
            cnt += 1
 
        # Check if there was a cycle
        if cnt != self.NumVertices:
            print ("There exists a cycle in the graph")
        else :
            # Print topological order
            print (top_order)

 
    def max_path_cpp(self) :
        
        for i in range(n_vertices):
            self.cost[i] = 0            
            self.cam_max[i] = 999
        max = 0
        for a in range(n_vertices) :
            v = self.ordely[a]
            for i in self.adj[v]:
                viz = i
                if self.cost[viz] < self.cost[v] + 1 :
                    self.cost[viz] = self.cost[v] + 1
                    if self.cost[viz] > max :
                        max = self.cost[viz]
        print("\nCusto maximo ", max)
 

    stack = []

    def topologicalSortUtil_cpp(self, v, vetorVisitado, stack):
        vetorVisitado[v] = True
        for q in self.adj[v]:
            if(not vetorVisitado[q]):
                self.topologicalSortUtil_cpp(q, vetorVisitado, stack)

        stack.append(v)



    def topologicalSortcpp(self):
        pilha = []
        vetorVisitado = [0]*self.V
        
        
        for t in range(self.V):
            if vetorVisitado[t] == False:
                self.topologicalSortUtil_cpp(t, vetorVisitado, pilha)




        while(len(pilha) != 0):
            
            self.ordely.append(pilha[-1])
            pilha.pop()
            

    def addEdge_cpp(self, v, w):
        self.adj[v].append(w)





        

g = Graph(n_vertices)
g.addEdge(0, 1);
g.addEdge(1, 4);
g.addEdge(0, 2);
g.addEdge(0, 3);
g.addEdge(1, 2);
g.addEdge(1, 3);
g.addEdge(2, 6);
g.addEdge(2, 5);
g.addEdge(2, 3);
g.addEdge(4, 5);
g.addEdge(4, 6);
g.addEdge(3, 4);


 
print ("Segue ordenacao topologica")
g.topologicalSort()




g2 = Graph(n_vertices)
g2.addEdge_cpp(0, 1);
g2.addEdge_cpp(1, 4);
g2.addEdge_cpp(0, 2);
g2.addEdge_cpp(0, 3);
g2.addEdge_cpp(1, 2);
g2.addEdge_cpp(1, 3);
g2.addEdge_cpp(2, 6);
g2.addEdge_cpp(2, 5);
g2.addEdge_cpp(2, 3);
g2.addEdge_cpp(4, 5);
g2.addEdge_cpp(4, 6);
g2.addEdge_cpp(3, 4);


g2.topologicalSortcpp()
print("\nOrdenacao topologica via aplicativo em cpp")
print(g2.ordely)
g2.max_path_cpp();

 
