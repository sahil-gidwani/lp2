from heapq import heappop, heappush

class PuzzleState:

    def __init__(self, puzzle, parent=None, move=""):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.g = 0
        self.h = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def calculate_heuristic(self):
        # manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                num = self.puzzle[i][j]
                if num != 0:
                    x = (num - 1) // 3
                    y = (num - 1) % 3
                    distance += abs(x - i) + abs(y - j)
        return distance

    def get_blank_position(self):
        # find the position of the blank tile (0)
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def generate_possible_moves(self):
        # generate possible moves by swapping the blank tile with adjacent tiles
        moves = []
        i, j = self.get_blank_position()

        if i > 0:
            moves.append(("UP", i - 1, j))
        if i < 2:
            moves.append(("DOWN", i + 1, j))
        if j > 0:
            moves.append(("LEFT", i, j - 1))
        if j < 2:
            moves.append(("RIGHT", i, j + 1))

        return moves

    def generate_child_states(self):
        # generate child states by applying possible moves
        child_states = []
        moves = self.generate_possible_moves()

        for move, x, y in moves:
            i, j = self.get_blank_position()  # get the position of the blank tile
            new_puzzle = [row[:] for row in self.puzzle]  # create a copy of the puzzle
            new_puzzle[i][j], new_puzzle[x][y] = new_puzzle[x][y], new_puzzle[i][j]
            child_states.append(PuzzleState(new_puzzle, parent=self, move=move))

        return child_states

    def print_solution(self):
        moves = []
        states = []
        node = self
        while node:
            moves.append(node.move)
            states.append(node.puzzle)
            node = node.parent

        moves.reverse()
        states.reverse()
        print("Solution Path:")
        for move, state in zip(moves, states):
            print("Move:", move)
            print("State:")
            for row in state:
                print(row)
            print("")

def solve_puzzle(start_state):
    open_list = []
    closed_set = set()

    start_state.g = 0
    open_list.append(start_state)

    while open_list:
        current_state = heappop(open_list)
        closed_set.add(tuple(map(tuple, current_state.puzzle)))

        if current_state.puzzle == goal_state:
            current_state.print_solution()
            return

        child_states = current_state.generate_child_states()
        for child_state in child_states:
            if tuple(map(tuple, child_state.puzzle)) not in closed_set:
                child_state.g = current_state.g + 1
                heappush(open_list, child_state)

start_state = PuzzleState([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solve_puzzle(start_state)
