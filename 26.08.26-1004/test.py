import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2), 6)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10)
    

if __name__ == '__main__':
    unittest.main()