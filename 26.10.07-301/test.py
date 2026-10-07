import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.removeInvalidParentheses("()())()"), ["(())()", "()()()"])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.removeInvalidParentheses("(a)())()"), ["(a())()", "(a)()()"])

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.removeInvalidParentheses(")("), [""])

if __name__ == '__main__':
    unittest.main()
