import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maxPalindromes("abaccdbbd", 3), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maxPalindromes("adbcda", 2), 0)

if __name__ == '__main__':
    unittest.main()
