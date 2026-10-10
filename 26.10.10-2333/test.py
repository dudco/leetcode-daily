import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minSumSquareDiff([1, 2, 3, 4], [2, 10, 20, 19], 0, 0), 579)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1), 43)

if __name__ == '__main__':
    unittest.main()
