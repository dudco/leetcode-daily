import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.checkOverlap(1, 0, 0, 1, -1, 3, 1), True)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.checkOverlap(1, 1, 1, 1, -3, 2, -1), False)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.checkOverlap(1, 0, 0, -1, 0, 0, 1), True)

if __name__ == '__main__':
    unittest.main()
