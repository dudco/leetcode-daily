import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.countIslands([[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]], 5), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.countIslands([[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3), 6)

if __name__ == '__main__':
    unittest.main()
