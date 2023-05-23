from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        # undirected graph 
        self.graph[u].append(v)
        self.graph[v].append(u)

    def displayGraph(self):
        for u in self.graph:
            print(u, " -> ", end="")
            for v in self.graph[u]:
                print(v, end=" ")
            print()

    def DFSUtil(self, v, visited):
        visited[v] = True

        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self):
        V = len(self.graph)
        visited = [False]*(V)

        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
        
        # self.DFSUtil(2, visited) # to start from a particular vertex

    def BFS(self, src):

        V = len(self.graph)
        visited = [False]*(V)

        queue = []

        queue.append(src)
        visited[src] = True

        while queue:
            v = queue.pop(0)
            print(v)

            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 3)

# take input for adding edges
# while True:
#     u = input("Enter the source vertex (or 'q' to quit): ")
#     if u == 'q':
#         break
#     v = input("Enter the destination vertex: ")
#     g.addEdge(int(u), int(v))

print("Graph:")
g.displayGraph()

print("Following is Depth First Traversal")
g.DFS()

print("Following is Breadth First Traversal (starting from vertex 0)")
g.BFS(0)
