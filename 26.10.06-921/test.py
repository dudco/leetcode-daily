import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minAddToMakeValid("((("), 3)

if __name__ == '__main__':
    unittest.main()
