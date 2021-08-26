import unittest

import numpy as np

from agent import Agent

class TestAgent(unittest.TestCase):

	def testGetPossibleMovesValidMoves(self):
		board = np.array([[2, 1, 1], [2, 1, 0], [0, 0, 0]])
		expected_results = {'211211000', '211210100', '211210010', '211210001'}

		cur_agent = Agent()
		self.assertEqual(set(cur_agent.get_possible_moves_from_state(board)),
						 expected_results)


	def testGetPossibleMovesTieGame(self):
		board = np.array([[2, 1, 1], [1, 2, 2], [2, 1, 1]])

		cur_agent = Agent()
		self.assertEqual(cur_agent.get_possible_moves_from_state(board), [])


	def testGetPossibleMovesOtherTeamWins(self):
		board = np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]])

		cur_agent = Agent()
		self.assertEqual(cur_agent.get_possible_moves_from_state(board), [])


	def testAgentTrainingSimple(self):
		board_one = '111000000'
		board_two = '000000000'
		board_sequence = [(board_one, True), (board_two, True)]

		cur_agent = Agent()
		cur_agent.init_value_function()
		cur_agent.train(board_sequence)

		# Need to build the value function ourselves.
		expected_result = {}
		with open('initial_value_states.txt', 'r') as f:
			for line in f:
				expected_result[line[3:44:5]] = float(line[-5:-2])

		expected_result[board_one] = 1.0
		expected_result[board_two] = 0.55

		self.assertEqual(cur_agent.value_function, expected_result)


	def testAgentTrainingMoreComplexWithExploratoryMove(self):
		board_one = '111000000'
		board_two = '110000000'
		board_three = '100000000'
		board_four = '000000000'
		board_sequence = [(board_one, True), (board_two, True),
						  (board_three, False), (board_four, True)]

		cur_agent = Agent()
		cur_agent.init_value_function()
		cur_agent.train(board_sequence)

		# Need to build the value function ourselves.
		expected_result = {}
		with open('initial_value_states.txt', 'r') as f:
			for line in f:
				expected_result[line[3:44:5]] = float(line[-5:-2])

		expected_result[board_one] = 1.0
		expected_result[board_two] = 0.55
		expected_result[board_three] = 0.5
		expected_result[board_four] = 0.55
		self.assertEqual(cur_agent.value_function, expected_result)


	def testAgentTrainingMoreComplexMultipleSequences(self):
		board_one = '111000000'
		board_two = '110000000'
		board_three = '100000000'
		board_four = '000000000'
		
		sequence_one = [(board_one, True), (board_two, True),
						(board_three, False), (board_four, True)]
		sequence_two = [(board_one, True), (board_two, True),
						(board_three, True), (board_four, True)]

		cur_agent = Agent()
		cur_agent.init_value_function()
		cur_agent.train(sequence_one)

		# Need to build the value function ourselves.
		expected_result = {}
		with open('initial_value_states.txt', 'r') as f:
			for line in f:
				expected_result[line[3:44:5]] = float(line[-5:-2])

		expected_result[board_one] = 1.0
		expected_result[board_two] = 0.55
		expected_result[board_three] = 0.5
		expected_result[board_four] = 0.55
		self.assertEqual(cur_agent.value_function, expected_result)

		# Let's train again.
		cur_agent.train(sequence_two)

		expected_result[board_one] = 1.0
		expected_result[board_two] = 0.595
		expected_result[board_three] = 0.5095
		expected_result[board_four] = 0.55095

		for key in [board_one, board_two, board_three, board_four]:
			print('Expected {}.  Got {}.'.format(
				expected_result[key], cur_agent.value_function[key]))
		self.assertEqual(cur_agent.value_function, expected_result)


if __name__ == '__main__':
	unittest.main()