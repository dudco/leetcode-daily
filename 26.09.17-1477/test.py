import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minSumOfLengths([3, 2, 2, 4, 3], 3), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minSumOfLengths([7, 3, 4, 7], 7), 2)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6), -1)

if __name__ == '__main__':
    unittest.main()
