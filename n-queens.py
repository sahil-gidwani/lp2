N = 8

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

# a utility function to check if a queen can be placed on board[row][col]
# note that this function is called when "col" queens are already placed in columns 
# from 0 to col -1 so we need to check only left side for attacking queens
def isSafeBT(board, row, col):
	# check this row on left side
	for i in range(col):
		if board[row][i] == 1:
			return False

	# check upper diagonal on left side
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	# check lower diagonal on left side
	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 1:
			return False

	return True

def solveNQUtilBT(board, col):
	# base case: if all queens are placed then return true
	if col >= N:
		return True

	# consider this column and try placing this queen in all rows one by one
	for i in range(N):

		if isSafeBT(board, i, col):
			# place this queen in board[i][col]
			board[i][col] = 1

			# recur to place rest of the queens
			if solveNQUtilBT(board, col + 1) == True:
				return True

			# if placing queen in board[i][col] doesn't lead to a solution, then 
            # queen from board[i][col]
			board[i][col] = 0

	# if the queen can not be placed in any row in this column col then return false
	return False

# an optimized function to check if a queen can be placed on board[row][col]
def isSafeBB(row, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):
	if (slashCodeLookup[slashCode[row][col]] or backslashCodeLookup[backslashCode[row][col]] or rowLookup[row]):
		return False
	return True

# a recursive utility function to solve N Queen problem
def solveNQueensUtilBB(board, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup):	
	# base case: If all queens are placed then return True
	if(col >= N):
		return True
	
	for i in range(N):
		if(isSafeBB(i, col, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)):
			# place this queen in board[i][col]
			board[i][col] = 1
			rowLookup[i] = True
			slashCodeLookup[slashCode[i][col]] = True
			backslashCodeLookup[backslashCode[i][col]] = True
			
			# recur to place rest of the queens
			if(solveNQueensUtilBB(board, col + 1, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup)):
				return True
			
			# if placing queen in board[i][col] doesn't lead to a solution, then backtrack
			# remove queen from board[i][col]
			board[i][col] = 0
			rowLookup[i] = False
			slashCodeLookup[slashCode[i][col]] = False
			backslashCodeLookup[backslashCode[i][col]] = False
			
	# if queen can not be place in any row in this column col then return False
	return False

# This function solves the N Queen problem using Backtracking. It mainly uses solveNQUtil() to
# solve the problem. It returns false if queens cannot be placed, otherwise return true and
# placement of queens in the form of 1s. note that there may be more than one
# solutions, this function prints one of the feasible solutions.
def solveNQBT():
	board = [[0 for _ in range(N)] for _ in range(N)]

	if solveNQUtilBT(board, 0) == False:
		print ("Solution does not exist")
		return False

	print("Solution by Backtracking")
	printSolution(board)
	return True

solveNQBT()

# This function solves the N Queen problem using Branch or Bound. It mainly uses solveNQueensUtil() to
# solve the problem. It returns False if queens cannot be placed,otherwise return True or
# prints placement of queens in the form of 1s. note that there may be more than one
# solutions,this function prints one of the feasible solutions
def solveNQueensBB():
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
	
	if(solveNQueensUtilBB(board, 0, slashCode, backslashCode, rowLookup, slashCodeLookup, backslashCodeLookup) == False):
		print("Solution does not exist")
		return False
		
	print("Solution by Branch and Bound")
	printSolution(board)

solveNQueensBB()
