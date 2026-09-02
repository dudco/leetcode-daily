import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.findKthSmallest([3,6,9], 3), 9)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.findKthSmallest([5,2], 7), 12)

    

if __name__ == '__main__':
    unittest.main()