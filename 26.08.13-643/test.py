import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = Solution()
    #     self.assertEqual(s.findMaxAverage([1,12,-5,-6,50,3], 4), 12.75000)
    # def test_case2(self):
    #     s = Solution()
    #     self.assertEqual(s.findMaxAverage([5], 1), 5.00000)
    # def test_case3(self):
    #     s = Solution()
    #     self.assertEqual(s.findMaxAverage([-1], 1), -1.00000)
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.findMaxAverage([0,4,0,3,2], 1), 4.00000)


if __name__ == '__main__':
    unittest.main()