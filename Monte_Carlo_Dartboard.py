from random import randint

# n darts d squares m dots in a single square

# Fires n darts randomly at d squares.
def dart_board(n,d):
	board = [0]*d
	for i in range(0,n):
		board[randint(0,d-1)] += 1
	return board

# For x dartboards counts how many have a square with at least m dots.
def count_board(n,d,m,x):
	total = 0
	for j in range(0,x):
		if any(dots >= m for dots in dart_board(n,d)):
			total += 1
	return total

# Approximates the probability of a dartboard having a square with at least m dots. 
def prob_count_board(n,d,m,x):
	return count_board(n,d,m,x)/x

# Counts number of dartboards where at least half the squares are empty out of x dartboards.
def half_squares_empty(n,d,x):
	total = 0
	for j in range(0,x):
		if dart_board(n,d).count(0) >= d/2:
			total += 1
	return total

# Approximates probability at least half the squares are empty.
def prob_half_squares_empty(n,d,x):
	return half_squares_empty(n,d,x)/x


print( prob_half_squares_empty(16, 16, 10000) )
