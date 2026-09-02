import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.isSubsequence("abc", "ahbgdc"), True)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.isSubsequence("axc", "ahbgdc"), False)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.isSubsequence("axc", "ajajxiwc"), True)

    

if __name__ == '__main__':
    unittest.main()