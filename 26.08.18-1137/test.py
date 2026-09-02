import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.tribonacci(4), 4)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.tribonacci(25), 1389537)
    

if __name__ == '__main__':
    unittest.main()