import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([1,1,0,1]), 3)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([0,1,1,1,0,1,1,0,1]), 5)

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([1,1,1]), 2)

    def test_case4(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([0,0,0]), 0)

    def test_case5(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([0,1,1]), 2)

    def test_case6(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([1,1,0]), 2)

    def test_case7(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([1,1,0,1,0,0,1,1,1,1,1,0]), 5)

    def test_case8(self):
        s = solution.Solution()
        self.assertEqual(s.longestSubarray([1,0,0,1,0]), 1)


if __name__ == '__main__':
    unittest.main()