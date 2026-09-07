import unittest

import solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.distinctSubseqII("abc"), 7)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.distinctSubseqII("aba"), 6)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.distinctSubseqII("aaa"), 3)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.distinctSubseqII("lee"), 5)

if __name__ == '__main__':
    unittest.main()
