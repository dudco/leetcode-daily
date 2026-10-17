import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minSwaps([37, 100]), 1)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minSwaps([22, 14, 33, 7]), 0)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minSwaps([18, 43, 34, 16]), 2)

if __name__ == '__main__':
    unittest.main()
