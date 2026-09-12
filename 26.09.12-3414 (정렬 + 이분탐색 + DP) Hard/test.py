import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maximumWeight([[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]]), [2, 3])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maximumWeight([[5, 8, 1], [6, 7, 7], [4, 7, 3], [9, 10, 6], [7, 8, 2], [11, 14, 3], [3, 5, 5]]), [1, 3, 5, 6])

if __name__ == '__main__':
    unittest.main()
