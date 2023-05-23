class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
	
	def addEdge(self, u, v, dist):
		# undirected graph 
		self.graph[u][v] = dist
		self.graph[v][u] = dist
	
	def displayGraph(self):
		for row in self.graph:
			for val in row:
				print(val, end="\t")
			print()

	def printSolution(self, dist):
		print("Vertex \t Distance from Source")
		for node in range(self.V):
			print(node, "\t\t", dist[node])

	# a utility function to find the vertex with minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):

		# initialize minimum distance for next node
		min = 1e7

		# search not nearest vertex not in the shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	def dijkstra(self, src):

		dist = [1e7] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for i in range(self.V):

			# pick the minimum distance vertex from the set of vertices not yet processed
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# put the minimum distance vertex in the shortest path tree
			sptSet[u] = True

			# update dist value of the adjacent vertices of the picked vertex only if the current
			# distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):
				if (self.graph[u][v] > 0 and
				sptSet[v] == False and
				dist[v] > dist[u] + self.graph[u][v]):
					dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]]

print("Graph:")
g.displayGraph()

g.dijkstra(0)
