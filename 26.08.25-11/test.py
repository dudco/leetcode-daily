import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.maxArea([1, 1]), 1)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.maxArea([8,7,2,1]), 7)

    

if __name__ == '__main__':
    unittest.main()