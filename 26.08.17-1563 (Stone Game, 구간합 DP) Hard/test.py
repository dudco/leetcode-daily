import unittest

from solution_dp import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.stoneGameV([6,2,3,4,5,5]), 18)

    def test_case2(self):
        s = Solution()
        self.assertEqual(s.stoneGameV([7,7,7,7,7,7,7]), 28)

    def test_case3(self):
        s = Solution()
        self.assertEqual(s.stoneGameV([4]), 0)

    def test_case4(self):
        s = Solution()
        self.assertEqual(s.stoneGameV([2,1,1]), 3)

    def test_case5(self):
        s = Solution()
        self.assertEqual(s.stoneGameV([1,1,2]), 3)

    def test_case6(self):
            s = Solution()
            self.assertEqual(s.stoneGameV([2,3,1,4]), 7)

if __name__ == '__main__':
    unittest.main()