import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1,2,3,4]), [24,12,8,6])
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([-1,1,0,-3,3]), [0,0,9,0,0])

    

if __name__ == '__main__':
    unittest.main()