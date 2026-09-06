import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.numDistinct("rabbbit", "rabbit"), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.numDistinct("babgbag", "bag"), 5)

if __name__ == '__main__':
    unittest.main()
