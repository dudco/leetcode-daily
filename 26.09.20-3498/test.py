import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.reverseDegree("abc"), 148)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.reverseDegree("zaza"), 160)

if __name__ == '__main__':
    unittest.main()
