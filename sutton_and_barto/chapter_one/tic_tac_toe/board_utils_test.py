import unittest

import numpy as np

import board_utils as board_utils

class TestBoardUtils(unittest.TestCase):

	def testBoardToHashCode(self):
		board = np.array([[0, 1, 1], [2, 1, 0], [0, 0, 0]])
		expected_result = '011210000'
		self.assertEqual(board_utils.board_to_hash_code(board), expected_result)

	def testBoardToHashCode(self):
		hash_code = '011210000'
		expected_result = np.array([[0, 1, 1], [2, 1, 0], [0, 0, 0]])
		self.assertTrue(np.array_equal(
			board_utils.hash_code_to_board(hash_code),
			expected_result))

	def testGetBoardStatus(self):
		# Ongoing
		board_one = np.array([[0, 1, 1], [2, 1, 0], [0, 0, 0]])
		# Tie
		board_two = np.array([[2, 1, 2], [1, 2, 1], [1, 2, 1]])
		# 'x' won
		board_three = np.array([[1, 0, 2], [0, 1, 2], [2, 2, 1]])
		# 'o' won
		board_four = np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]])

		self.assertEqual(board_utils.get_board_status(board_one), 0)
		self.assertEqual(board_utils.get_board_status(board_two), 0)
		self.assertEqual(board_utils.get_board_status(board_three), 1)
		self.assertEqual(board_utils.get_board_status(board_four), 2)

	def testGetInitialBoardValue(self):
		# Ongoing
		board_one = np.array([[0, 1, 1], [2, 1, 0], [0, 0, 0]])
		# Tie
		board_two = np.array([[2, 1, 2], [1, 2, 1], [1, 2, 1]])
		# 'x' won
		board_three = np.array([[1, 0, 2], [0, 1, 2], [2, 2, 1]])
		# 'o' won
		board_four = np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]])

		self.assertEqual(board_utils.get_initial_board_value(board_one), 0.5)
		self.assertEqual(board_utils.get_initial_board_value(board_two), 0.5)
		self.assertEqual(board_utils.get_initial_board_value(board_three), 1.0)
		self.assertEqual(board_utils.get_initial_board_value(board_four), 0.0)

if __name__ == '__main__':
	unittest.main()