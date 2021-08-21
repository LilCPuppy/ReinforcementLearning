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
		board: An [[int]] representing the current state.
	Returns:
		A string of 0, 1, or 2 representing the board.
	'''
	char_list = []
	for row in board:
		char_list.extend([str(elem) for elem in row])
	return ''.join(char_list)