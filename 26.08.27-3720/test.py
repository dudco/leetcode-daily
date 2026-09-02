import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("abc", "bba"), "bca")
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("leet", "code"), "eelt")
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("baba", "bbaa"), "")
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("baba", "bbaa"), "")
    def test_case5(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("aa", "ab"), "")
    def test_case6(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("aaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbb", "aaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbb"), "")
    def test_case7(self):
        s = Solution()
        self.assertEqual(s.lexGreaterPermutation("z", "a"), "z")
    def test_case8(self):
            s = Solution()
            self.assertEqual(s.lexGreaterPermutation("ab", "ab"), "ba")
    

if __name__ == '__main__':
    unittest.main()