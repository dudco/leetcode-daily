import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.sortPermutation([0, 3, 2, 1]), 1)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.sortPermutation([0, 1, 3, 2]), 2)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.sortPermutation([3, 2, 1, 0]), 0)

if __name__ == '__main__':
    unittest.main()
