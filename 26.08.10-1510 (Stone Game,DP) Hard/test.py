import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.winnerSquareGame(1), True)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.winnerSquareGame(2), False)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.winnerSquareGame(4), True)


if __name__ == '__main__':
    unittest.main()