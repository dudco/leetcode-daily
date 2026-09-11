import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.totalNumbers([1, 2, 3, 4]), 12)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.totalNumbers([0, 2, 2]), 2)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.totalNumbers([6, 6, 6]), 1)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.totalNumbers([1, 3, 5]), 0)

if __name__ == '__main__':
    unittest.main()
