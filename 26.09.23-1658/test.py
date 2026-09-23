import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minOperations([1, 1, 4, 2, 3], 5), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minOperations([5, 6, 7, 8, 9], 4), -1)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minOperations([3, 2, 20, 1, 1, 3], 10), 5)

if __name__ == '__main__':
    unittest.main()
