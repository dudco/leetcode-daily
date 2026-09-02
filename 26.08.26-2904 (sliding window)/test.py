import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = Solution()
    #     self.assertEqual(s.shortestBeautifulSubstring("100011001", 3), "11001")
    # def test_case2(self):
    #     s = Solution()
    #     self.assertEqual(s.shortestBeautifulSubstring("1011", 2), "11")
    # def test_case3(self):
    #         s = Solution()
    #         self.assertEqual(s.shortestBeautifulSubstring("000", 1), "")
    # def test_case4(self):
    #         s = Solution()
    #         self.assertEqual(s.shortestBeautifulSubstring("10100010", 5), "")
    def test_case5(self):
            s = Solution()
            self.assertEqual(s.shortestBeautifulSubstring("1100001110111100100", 8), "11101111001")
    

if __name__ == '__main__':
    unittest.main()