class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
					for row in range(vertices)]
	
	def addEdge(self, u, v, dist):
		# undirected graph 
		self.graph[u][v] = dist
		self.graph[v][u] = dist
	
	def displayGraph(self):
		for row in self.graph:
			for val in row:
				print(val, end="\t")
			print()

	def printMST(self, parent):
		print("Edge \tWeight")
		for i in range(1, self.V):
			print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

	# a utility function to find the vertex with minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minKey(self, key, mstSet):
		min = 1e7

		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v

		return min_index

	def primMST(self):
		# key values used to pick minimum weight edge in cut
		key = [1e7] * self.V
		# array to store constructed MST
		parent = [None] * self.V
		# make key 0 so that this vertex is picked as first vertex
		key[0] = 0
		mstSet = [False] * self.V

		# first node is always the root of
		parent[0] = -1 

		for _ in range(self.V):
			# pick the minimum distance vertex from the set of vertices not yet processed
			# u is always equal to src in first iteration
			u = self.minKey(key, mstSet)

			# put the minimum distance vertex in the shortest path tree
			mstSet[u] = True

			# update dist value of the adjacent vertices of the picked vertex only if the current
			# distance is greater than new distance and the vertex in not in the shortest path tree
			for v in range(self.V):

				# graph[u][v] is non zero only for adjacent vertices of m
				# mstSet[v] is false for vertices not yet included in MST
				# update the key only if graph[u][v] is smaller than key[v]
				if self.graph[u][v] > 0 and mstSet[v] == False \
				and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u

		self.printMST(parent)



g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
		[2, 0, 3, 8, 5],
		[0, 3, 0, 0, 7],
		[6, 8, 0, 0, 9],
		[0, 5, 7, 9, 0]]

print("Graph:")
g.displayGraph()

g.primMST()
