import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.pivotIndex([1,7,3,6,5,6]), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.pivotIndex([1,2,3]), -1)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.pivotIndex([2,1,-1]), 0)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.pivotIndex([-1,1,2]), 2)

if __name__ == '__main__':
    unittest.main()