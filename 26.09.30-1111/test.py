import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maxDepthAfterSplit("(()())"), [0, 1, 1, 1, 1, 0])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maxDepthAfterSplit("()(())()"), [0, 0, 0, 1, 1, 0, 1, 1])

if __name__ == '__main__':
    unittest.main()
