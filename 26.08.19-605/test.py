import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.canPlaceFlowers([1,0,0,0,1], 1), True)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.canPlaceFlowers([1,0,0,0,1], 2), False)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.canPlaceFlowers([1,0,0,0,0,1], 2), False)
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.canPlaceFlowers([1,0,1,0,1,0,1], 0), True)
    def test_case5(self):
        s = Solution()
        self.assertEqual(s.canPlaceFlowers([1,0,0,0,1,0,0], 2), True)

    

if __name__ == '__main__':
    unittest.main()