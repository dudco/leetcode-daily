import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maxSumOfSquares(2, 3), "30")

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maxSumOfSquares(2, 17), "98")

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.maxSumOfSquares(1, 10), "")

if __name__ == '__main__':
    unittest.main()
