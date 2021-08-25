import numpy as np

import board_utils as board_utils

class Agent:

	def __init__(self):
		self.value_function = {}
		self.step_size = 0.1


	def init_value_function(self):
		with open('initial_value_states.txt', 'r') as f:
			for line in f:
				self.value_function[line[3:44:5]] = float(line[-5:-2])


	def get_possible_moves_from_state(self, state):
		'''Return a list of hash codes for possible moves.

		Args:
			board: A [[int]] numpy array.

		Returns:
			A [string] list representing the hash codes for subsequent/possible
			moves.
		'''
		if board_utils.get_board_status(state) != 0:
			# No possible moves.
			return []

		if not np.any(state == 0):
			# Was a tie game
			return []

		result = []
		open_indices = np.argwhere(state == 0)
		for index in open_indices:
			current_state = state.copy()
			current_state[index[0], index[1]] = 1
			result.append(board_utils.board_to_hash_code(current_state))

		return result


	def train(self, state_hash_sequence):
		'''Train the model based on the non-exploratory moves.

		The sequence is in *reverse* order, and only pertains to the state
		*after* our agent has moved.  For states that were the result of
		exploratory moves, we don't update the value function.

		Args:
			state_sequence: A [(string, bool)] list where the state is encoded
			as a string hash code, and the bool is refers to if the move was
			exploiting rather than exploring.
		Returns:
			A reference to the value function.
		'''
		previous_state, was_exploiting = state_hash_sequence[0]
		for index, pair in enumerate(state_hash_sequence[1:]):
			if not was_exploiting:
				continue

			current_state_value = self.value_function[pair[0]]
			previous_state_value = self.value_function[previous_state]

			# Update the state function
			self.value_function[pair[0]] += (self.step_size *
				(previous_state_value - current_state_value))

		return self.value_function
