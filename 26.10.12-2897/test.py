import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maxSum([2, 6, 5, 8], 2), 261)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maxSum([4, 5, 4, 7], 3), 90)

if __name__ == '__main__':
    unittest.main()
