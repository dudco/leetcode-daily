import unittest

import solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.uniformArray([2,3]), True)

    # def test_case2(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.uniformArray([4,6]), True)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.uniformArray([23,86]), True)

if __name__ == '__main__':
    unittest.main()