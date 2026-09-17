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

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.minSumOfLengths([1, 6, 1], 7), -1)

    def test_case5(self):
        s = solution.Solution()
        self.assertEqual(s.minSumOfLengths([2,1,3,3,2,3,1], 6), 5)

    def test_case6(self):
        s = solution.Solution()
        self.assertEqual(s.minSumOfLengths([1,1,1,2,2,2,4,4], 6), 6)


if __name__ == '__main__':
    unittest.main()
