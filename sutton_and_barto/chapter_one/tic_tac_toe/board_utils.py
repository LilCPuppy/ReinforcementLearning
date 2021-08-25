import numpy as np

def board_to_hash_code(board):
	'''Converts board to a string for hashing.

	The hash code will read the board left to right, top to bottom and place a
	'0' for an empty slot, a '1' for a 1 ('x' plays as 1), and a '2' for a 2
	('o' plays as 2).

	Example:
		[[0, 1, 1], [2, 1, 0], [0, 0, 0]] -> '011210000'

	This is a bijective relationship (since we can invert it), so we need not
	worry about issues of mapping two board states to the same hash.

	Args:
		board: An [[int]] np array representing the current state.
	Returns:
		A string of 0, 1, or 2 representing the board.
	'''
	char_list = []
	for row in board:
		char_list.extend([str(elem) for elem in row])
	return ''.join(char_list)


def hash_code_to_board(board_hash):
	'''Converts a ternary string to a board hash.

	Args:
		board_hash: A string length nine consisting of '0', '1', and '2'.
	Returns:
		The corresponding np.array representing the state.
	'''
	board = np.array([int(char) for char in board_hash])
	return board.reshape((3, 3))


def get_board_status(board):
	'''Get the status of the board, 1 is 'x' won, 2 is 'o' won, and 0 otherwise.

	Args:
		board: A [[int]] np array representing the current state.
	Returns: 
		An integer encoding the termination status of this game.
	'''
	flat_board = board.flatten()
	winning_indices = [
		[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
		[0, 4, 8], [6, 4, 2]
	]
	for indices in winning_indices:
		cur_line = flat_board[np.array(indices)]
		if np.array_equal(cur_line, [1, 1, 1]):
			return 1
		elif np.array_equal(cur_line, [2, 2, 2]):
			return 2
	return 0

def get_initial_board_value(board):
	'''Get the initial value of the board as stated by the algorithm.

	Args:
		board: A 3x3 numpy array.
	Returns:
		The numerical initial value.  1.0 for 'x' winning, 0.0 for '0' winning,
		and 0.5 otherwise.
	'''
	status = get_board_status(board)
	if status == 1:
		return 1.0
	elif status == 2:
		return 0.0
	else:
		return 0.5