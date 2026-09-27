import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.reverseParentheses("(abcd)"), "dcba")

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.reverseParentheses("(u(love)i)"), "iloveu")

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.reverseParentheses("(ed(et(oc))el)"), "leetcode")

if __name__ == '__main__':
    unittest.main()
