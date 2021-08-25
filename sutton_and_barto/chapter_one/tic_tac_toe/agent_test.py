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


if __name__ == '__main__':
	unittest.main()