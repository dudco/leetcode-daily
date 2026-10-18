import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.numOfWays([2, 1, 3]), 1)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.numOfWays([3, 4, 5, 1, 2]), 5)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.numOfWays([1, 2, 3]), 0)

if __name__ == '__main__':
    unittest.main()
