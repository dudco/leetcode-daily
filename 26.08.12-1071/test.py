import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.gcdOfStrings("ABCABC", "ABC"), "ABC")
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.gcdOfStrings("ABABAB", "ABAB"), "AB")
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.gcdOfStrings("AAAAAB", "AAAA"), "")
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.gcdOfStrings("LEET", "CODE"), "")
    # def test_case5(self):
    #     s = Solution()
    #     self.assertEqual(s.maxSubarrayLength([2,2,3], 1), 2)


if __name__ == '__main__':
    unittest.main()