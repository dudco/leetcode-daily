import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maxAlternatingSum([1, 2, 3]), 12)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maxAlternatingSum([1, -1, 2, -2, 3, -3]), 16)

if __name__ == '__main__':
    unittest.main()
