import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.uniqueOccurrences([1,2,2,1,1,3]), True)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.uniqueOccurrences([1,2]), False)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.uniqueOccurrences( [-3,0,1,-3,1,1,1,-3,10,0]), True)


if __name__ == '__main__':
    unittest.main()