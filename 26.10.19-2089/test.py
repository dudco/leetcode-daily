import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.targetIndices([1, 2, 5, 2, 3], 2), [1, 2])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.targetIndices([1, 2, 5, 2, 3], 3), [3])

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.targetIndices([1, 2, 5, 2, 3], 5), [4])

if __name__ == '__main__':
    unittest.main()
