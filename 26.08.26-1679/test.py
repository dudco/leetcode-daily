import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.maxOperations([1,2,3,4], 5), 2)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.maxOperations([3,1,3,4,3], 6), 1)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.maxOperations([3,1,2,4,3], 4), 1)
    

if __name__ == '__main__':
    unittest.main()