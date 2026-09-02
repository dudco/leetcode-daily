import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.resultArray([2,1,3]), [2,3,1])
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.resultArray([5,4,3,8]), [5,3,4,8])

    

if __name__ == '__main__':
    unittest.main()