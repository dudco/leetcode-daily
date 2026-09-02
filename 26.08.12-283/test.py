import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.moveZeroes( [0]))
    
if __name__ == '__main__':
    unittest.main()