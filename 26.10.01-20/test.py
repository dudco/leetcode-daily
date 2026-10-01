import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.isValid("()"), True)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.isValid("()[]{}"), True)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.isValid("(]"), False)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.isValid("([])"), True)

    def test_case5(self):
        s = solution.Solution()
        self.assertEqual(s.isValid("([)]"), False)

if __name__ == '__main__':
    unittest.main()
