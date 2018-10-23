######NEWLIFE######
import random
import time

DEAD = ' '
LIVE = 'O'

#build a dead state board
def dead_state(height,width):
	"""Return a board fully filled out with dead state"""
	return [[DEAD for _ in range(0,width)]for _ in range(0,height)]

#get height and width of board
def get_height(board):
	"""Get the height(length of outer array) of input board"""
	return len(board)

def get_width(board):
	"""Get the width(length of inner array) of input board"""
	return len(board[0])
	
#build a random state board
def random_state(height,width):
	"""Return a board with randomized states(dead or live)"""
	random_board = dead_state(height,width)
	x_height = get_height(random_board)
	y_width = get_width(random_board)
	
	for x in range(0,x_height):
		for y in range(0,y_width):
			random_int = random.random()
			if random_int > .9:
				cell_state = LIVE
			else:
				cell_state = DEAD
			random_board[x][y] = cell_state
	return random_board

#render an input board
def render(board):
	"""Pretty print an input board"""
	x_height = get_height(board)
	y_width = get_width(board)
	
	print(" " + ("-" * y_width))
	for row in range(0,x_height):
		print("|" + ''.join(board[row]) + "|")
	print(" " + ("-" * y_width))
	
#calculate the next cell state
def get_next_cell(coords,inputboard):
	"""Calculate the next state of an individual cell"""
 	x = coords[0]
	y = coords[1]
	height = get_height(inputboard)
	width = get_width(inputboard)
	n_neighbors = 0
	
	for x1 in range(x-1,(x+1)+1):
		if x1 < 0 or x1 >= height: continue
		
		for y1 in range(y-1,(y+1)+1):
			if (y1 < 0 or y1 >= width): continue
			if (x1 == x and y1 == y): continue 
			if inputboard[x1][y1] == LIVE:
				n_neighbors += 1
	
	if inputboard[x][y] == LIVE:
		if n_neighbors <= 1:
			cell_state = DEAD
		if n_neighbors <=3:
			cell_state = LIVE
		else:
			cell_state = DEAD
	
	if inputboard[x][y] == DEAD:
		if n_neighbors == 3:
			cell_state = LIVE
		else:
			cell_state = DEAD
	
	return cell_state
	
	
	
#calculate the next state of board based on neighbor parameters
def get_next_state(board):
	"""Calculate the next state of the board"""
	x_height = get_height(board)
	y_width = get_width(board)
	new_board = dead_state(x_height,y_width)
	
	for x in range(0,x_height):
		for y in range(0,y_width):
			next_cell = get_next_cell((x,y),board)
			new_board[x][y] = next_cell
			
	return new_board

#run the program infinitely
 
def run_program(init_state):
	next_state = init_state
	while True:
		render(next_state)
		next_state = get_next_state(next_state)
		time.sleep(.03)
		
new_random_board = random_state(20,40)		
run_program(new_random_board)
