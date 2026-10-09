import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minInsertions("(()))"), 1)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minInsertions("())"), 0)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minInsertions("))())("), 3)

if __name__ == '__main__':
    unittest.main()
