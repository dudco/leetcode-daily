import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minCost([[1, 2], [3, 4]]), 6)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minCost([[6, 7], [5, 8]]), 9)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minCost([[2, 7, 5]]), 0)

if __name__ == '__main__':
    unittest.main()
