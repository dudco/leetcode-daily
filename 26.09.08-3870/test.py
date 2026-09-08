import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.countCommas(1002), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.countCommas(998), 0)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.countCommas(2019), 1020)

if __name__ == '__main__':
    unittest.main()
