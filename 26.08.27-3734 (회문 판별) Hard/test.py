import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.lexPalindromicPermutation("baba", "abba"), "baab")
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.lexPalindromicPermutation("baba", "bbaa"), "")
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.lexPalindromicPermutation("aac", "abb"), "aca")
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.lexPalindromicPermutation("abc", "abb"), "")

if __name__ == '__main__':
    unittest.main()