import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minOperations([0, 2, 1]), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minOperations([1, 0, 2]), 2)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minOperations([2, 0, 1, 3]), -1)

if __name__ == '__main__':
    unittest.main()
