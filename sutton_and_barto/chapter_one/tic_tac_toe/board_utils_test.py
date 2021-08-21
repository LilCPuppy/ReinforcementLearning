import unittest

import board_utils as board_utils

class TestBoardUtils(unittest.TestCase):

	def testBoardToHashCode(self):
		board = [[0, 1, 1], [2, 1, 0], [0, 0, 0]]
		expected_result = '011210000'
		self.assertEqual(board_utils.board_to_hash_code(board), expected_result)

if __name__ == '__main__':
	unittest.main()