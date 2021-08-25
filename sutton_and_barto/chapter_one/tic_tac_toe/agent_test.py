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


	def testAgentTraining(self):
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



if __name__ == '__main__':
	unittest.main()