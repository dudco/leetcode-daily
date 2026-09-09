import unittest

import solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.countCommas(1002), 3)

    # def test_case2(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.countCommas(998), 0)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.countCommas(1004590), 1008182)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.countCommas(1122872257463), 3490488028856)

if __name__ == '__main__':
    unittest.main()
