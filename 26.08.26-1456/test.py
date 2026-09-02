import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.maxVowels("abciiidef", 3), 3)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.maxVowels("aeiou", 2), 2)
    def test_case3(self):
            s = Solution()
            self.assertEqual(s.maxVowels("leetcode", 3), 2)
    

if __name__ == '__main__':
    unittest.main()