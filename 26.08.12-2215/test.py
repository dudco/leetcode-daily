import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.findDifference([1,2,3], [2,4,6]), [[1,3],[4,6]])
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.findDifference([1,2,3,3], [1,1,2,2]), [[3],[]])
    # def test_case3(self):
    #     s = Solution()
    #     self.assertEqual(s.maxSubarrayLength([5,5,5,5,5,5,5], 4), 4)
    # def test_case4(self):
    #     s = Solution()
    #     self.assertEqual(s.maxSubarrayLength([1], 1), 1)
    # def test_case5(self):
    #     s = Solution()
    #     self.assertEqual(s.maxSubarrayLength([2,2,3], 1), 2)


if __name__ == '__main__':
    unittest.main()