class Graph():

	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

	# a utility function to check if the current color assignment is safe for vertex v
	def isSafe(self, v, colour, c):
		for i in range(self.V):
			# check adjacent vertices if they exist and if they have the same color c
			if self.graph[v][i] == 1 and colour[i] == c:
				return False
		return True

	# a recursive utility function to solve m coloring problem
	def graphColourUtil(self, m, colour, v):
		# base case: if all vertices are assigned a color then return true
		if v >= self.V:
			return True

		# consider this vertex v and try different colors
		for c in range(1, m + 1):
			if self.isSafe(v, colour, c) == True:
				colour[v] = c
				# recur to color rest of the vertices
				if self.graphColourUtil(m, colour, v + 1) == True:
					return True
				# if assigning color c doesn't lead to a solution then remove it
				colour[v] = 0

	def graphColouring(self, m):
		colour = [0] * self.V
		if self.graphColourUtil(m, colour, 0) != True:
			print("No solution exists")
			return False

		print("Solution exists and the assigned colors are:")
		for c in colour:
			print(c, end=' ')
		return True

g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3

g.graphColouring(m)

# Time Complexity: O(m^V). There is a total of O(m^V) combinations of colors. 
# The upper bound time complexity remains the same but the average time taken will be less.
# Auxiliary Space: O(V). The recursive Stack of the graph coloring function will require O(V) space.