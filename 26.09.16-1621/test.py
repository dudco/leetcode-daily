import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.numberOfSets(4, 2), 5)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.numberOfSets(3, 1), 3)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.numberOfSets(30, 7), 796297179)

if __name__ == '__main__':
    unittest.main()
