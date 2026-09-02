import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.countBits(2), [0, 1, 1])
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.countBits(5), [0,1,1,2,1,2])
    

if __name__ == '__main__':
    unittest.main()