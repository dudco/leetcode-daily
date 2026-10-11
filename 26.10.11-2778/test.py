import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.sumOfSquares([1, 2, 3, 4]), 21)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.sumOfSquares([2, 7, 1, 19, 18, 3]), 63)

if __name__ == '__main__':
    unittest.main()
