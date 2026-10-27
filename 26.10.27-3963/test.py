import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.createGrid(2, 3), ["..#", "#.."])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.createGrid(3, 3), ["..#", "#..", "##."])

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.createGrid(1, 4), ["...."])

if __name__ == '__main__':
    unittest.main()
