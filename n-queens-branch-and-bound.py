N = 8

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

# an optimized function to check if a queen can be placed on board[row][col]
def isSafe(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
	if (slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row]):
		return False
	return True

# a recursive utility function to solve N Queen problem
def solveNQueensUtil(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):	
	# base case: If all queens are placed then return True
	if(col >= N):
		return True
	
	for i in range(N):
		if(isSafe(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)):
			# place this queen in board[i][col]
			board[i][col] = 1
			rowLookup[i] = True
			slashCodeLookup[slashCode[i][col]] = True
			backslashCodeLookup[backslashCode[i][col]] = True
			
			# recur to place rest of the queens
			if(solveNQueensUtil(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)):
				return True
			
			# if placing queen in board[i][col] doesn't lead to a solution, then backtrack
			# remove queen from board[i][col]
			board[i][col] = 0
			rowLookup[i] = False
			slashCodeLookup[slashCode[i][col]] = False
			backslashCodeLookup[backslashCode[i][col]] = False
			
	# if queen can not be place in any row in this column col then return False
	return False

# This function solves the N Queen problem using Branch or Bound. It mainly uses solveNQueensUtil() to
# solve the problem. It returns False if queens cannot be placed,otherwise return True or
# prints placement of queens in the form of 1s. note that there may be more than one
# solutions,this function prints one of the feasible solutions
def solveNQueens():
	board = [[0 for _ in range(N)] for _ in range(N)]
	
	# helper matrices
	slashCode = [[0 for _ in range(N)] for _ in range(N)]
	backslashCode = [[0 for _ in range(N)] for _ in range(N)]
	
	# arrays to tell us which rows are occupied
	rowLookup = [False] * N
	
	# keep two arrays to tell us which diagonals are occupied
	x = 2 * N - 1
	slashCodeLookup = [False] * x
	backslashCodeLookup = [False] * x
	
	# initialize helper matrices
	for rr in range(N):
		for cc in range(N):
			slashCode[rr][cc] = rr + cc
			backslashCode[rr][cc] = rr - cc + (N - 1)
	
	if(solveNQueensUtil(board, 0, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup) == False):
		print("Solution does not exist")
		return False
		
	printSolution(board)
	return True

solveNQueens()

# Time Complexity: The time complexity of the solver algorithm is O(N!), 
# where N is the number of rows and columns in the square board. 
# This is because for each column, the algorithm tries to place a queen in each row and 
# then recursively tries to place the queens in the remaining columns. 
# The number of possible combinations of queen placements in the board is N! since there can 
# be only one queen in each row and each column.

# Space Complexity: The space complexity of the solver algorithm is O(N^2), 
# where N is the number of rows and columns in the square board. T
# his is because we are using a 2D vector to represent the board, which takes up N^2 space. 
# Additionally, we are using three boolean arrays to keep track of the occupied rows and diagonals, 
# which take up 2N-1 space each. Therefore, the total space complexity is O(N^2 + 6N – 3), 
# which is equivalent to O(N^2).