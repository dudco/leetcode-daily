import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.missingInteger([1,2,3,2,5]), 6)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.missingInteger([3,4,5,1,12,14,13]), 15)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.missingInteger([1,3,4,5,12,14,13]), 2)
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.missingInteger([29,30,31,32,33,34,35,36,37]), 297)
    def test_case5(self):
        s = Solution()
        self.assertEqual(s.missingInteger([38]), 39)
    def test_case6(self):
        s = Solution()
        self.assertEqual(s.missingInteger([18,19,20,21,22,23,24,25,26,27,28,9]), 253)
    def test_case7(self):
        s = Solution()
        self.assertEqual(s.missingInteger([37,1,2,9,5,8,5,2,9,4]), 38)
    def test_case8(self):
        s = Solution()
        self.assertEqual(s.missingInteger([14,9,6,9,7,9,10,4,9,9,4,4]), 15)


if __name__ == '__main__':
    unittest.main()