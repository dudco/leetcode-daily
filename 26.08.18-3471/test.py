import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.largestInteger([3,9,2,1,7], 3), 7)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.largestInteger([3,9,7,2,1,7], 4), 3)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.largestInteger([0, 0], 1), -1)
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.largestInteger([0, 0], 2), 0)
    

if __name__ == '__main__':
    unittest.main()