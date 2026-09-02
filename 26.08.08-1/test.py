import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.twoSum([-1,-2,-3,-4,-5], -8), [2, 4])


if __name__ == '__main__':
    unittest.main()