import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]), True)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]), False)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.isRectangleOverlap([0, 0, 1, 1], [2, 2, 3, 3]), False)

if __name__ == '__main__':
    unittest.main()
