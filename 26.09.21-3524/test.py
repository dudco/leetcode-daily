import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.resultArray([1, 2, 3, 4, 5], 3), [9, 2, 4])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.resultArray([1, 2, 4, 8, 16, 32], 4), [18, 1, 2, 0])

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.resultArray([1, 1, 2, 1, 1], 2), [9, 6])

if __name__ == '__main__':
    unittest.main()
