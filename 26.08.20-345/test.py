import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.reverseVowels("IceCreAm"), "AceCreIm")
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.reverseVowels("leetcode"), "leotcede")

    

if __name__ == '__main__':
    unittest.main()