import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.countDaysTogether("08-15", "08-18", "08-16", "08-19"), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.countDaysTogether("10-01", "10-31", "11-01", "12-31"), 0)

if __name__ == '__main__':
    unittest.main()
