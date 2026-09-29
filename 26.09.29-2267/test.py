import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.hasValidPath([["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]), True)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.hasValidPath([[")", ")"], ["(", "("]]), False)

if __name__ == '__main__':
    unittest.main()
