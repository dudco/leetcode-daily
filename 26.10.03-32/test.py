import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.longestValidParentheses("(()"), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.longestValidParentheses(")()())"), 4)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.longestValidParentheses(""), 0)

if __name__ == '__main__':
    unittest.main()
