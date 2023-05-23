class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    def isSafe(self, v, color, c):
        for i in range(self.V):
            if (
                self.graph[v][i] == 1
                and color[i] == c
            ):
                return False
        return True

    def graphColorUtil(self, m, color, v, num_colors):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, color, c):
                color[v] = c

                # check if pruning is possible
                if (
                    num_colors + 1 < self.graphColorUtil(
                        m, color, v + 1, num_colors + 1
                    )
                ):
                    color[v] = 0
                    continue

                if self.graphColorUtil(m, color, v + 1, num_colors + 1):
                    return True
                color[v] = 0

        return False

    def graphColoring(self, m):
        color = [0] * self.V
        num_colors = 0

        if not self.graphColorUtil(m, color, 0, num_colors):
            print("No solution exists.")
            return

        print("Solution exists and the assigned colors are:")
        for c in color:
            print(c, end=" ")
        print()


g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3

g.graphColoring(m)
