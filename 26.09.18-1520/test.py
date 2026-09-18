import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.maxNumOfSubstrings("adefaddaccc"), ["e", "f", "ccc"])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.maxNumOfSubstrings("abbaccd"), ["d", "bb", "cc"])

if __name__ == '__main__':
    unittest.main()
