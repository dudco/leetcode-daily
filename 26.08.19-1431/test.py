import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.kidsWithCandies([2,3,5,1,3], 3), [True,True,True,False,True])
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.kidsWithCandies([4,2,1,1,2], 1), [True,False,False,False,False])
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.kidsWithCandies([12,1,12], 10), [True,False,True])

    

if __name__ == '__main__':
    unittest.main()