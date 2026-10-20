import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.sortableIntegers([3, 1, 2]), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.sortableIntegers([7, 6, 5]), 0)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.sortableIntegers([5, 8]), 3)

if __name__ == '__main__':
    unittest.main()
