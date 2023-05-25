from heapq import heappop, heappush

class Graph:
    def __init__(self, vertices, heuristics):
        self.vertices = vertices
        self.adjacency_list = {}
        self.heuristics = heuristics

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def heuristic(self, current, goal):
        return self.heuristics[current]

    def astar(self, start, goal):
        open_set = [(0, start)]  # Priority queue of nodes to explore
        came_from = {}  # Dictionary to track the optimal path
        g_score = {vertex: float('inf') for vertex in self.vertices}  # Cost from start to each vertex
        g_score[start] = 0
        f_score = {vertex: float('inf') for vertex in self.vertices}  # Estimated total cost from start to goal via each vertex
        f_score[start] = self.heuristic(start, goal)

        while open_set:
            current_cost, current = heappop(open_set)

            if current == goal:
                return self.reconstruct_path(came_from, current)

            for neighbor, weight in self.adjacency_list.get(current, []):
                tentative_g_score = g_score[current] + weight

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))

        return None  # No path found

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]

heuristics = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 3, 'F': 1, 'G': 0}

g = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'], heuristics)
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'E', 3)
g.add_edge('D', 'F', 6)
g.add_edge('E', 'F', 2)
g.add_edge('E', 'G', 3)
g.add_edge('F', 'G', 1)

start_vertex = 'A'
goal_vertex = 'G'

optimal_path = g.astar(start_vertex, goal_vertex)
if optimal_path:
    print("Optimal Path:", ' -> '.join(optimal_path))
else:
    print("No path found")