import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.generateParenthesis(1), ["()"])

if __name__ == '__main__':
    unittest.main()
