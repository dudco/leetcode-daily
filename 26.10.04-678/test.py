import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.checkValidString("()"), True)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.checkValidString("(*)"), True)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.checkValidString("(*))"), True)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.checkValidString("("), False)

if __name__ == '__main__':
    unittest.main()
