import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.firstStableIndex([5, 0, 1, 4], 3), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.firstStableIndex([3, 2, 1], 1), -1)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.firstStableIndex([0], 0), 0)

if __name__ == '__main__':
    unittest.main()
