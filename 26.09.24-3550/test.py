import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.smallestIndex([1, 3, 2]), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.smallestIndex([1, 10, 11]), 1)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.smallestIndex([1, 2, 3]), -1)

if __name__ == '__main__':
    unittest.main()
