import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.minMoves(["S.", "XL"], 2), 2)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.minMoves(["LS", "RL"], 4), 3)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.minMoves(["L.S", "RXL"], 3), -1)

if __name__ == '__main__':
    unittest.main()