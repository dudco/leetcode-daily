import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.palindromePath(3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]), [True, False])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.palindromePath(4, [[0, 1], [0, 2], [0, 3]], "abca", ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"]), [False, False, True])

if __name__ == '__main__':
    unittest.main()
