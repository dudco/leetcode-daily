import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.sumCounts([1, 2, 1]), 15)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.sumCounts([2, 2]), 3)

if __name__ == '__main__':
    unittest.main()
