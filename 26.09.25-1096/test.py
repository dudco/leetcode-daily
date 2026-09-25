import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.braceExpansionII("{a,b}{c,{d,e}}"), ["ac", "ad", "ae", "bc", "bd", "be"])

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.braceExpansionII("{{a,z},a{b,c},{ab,z}}"), ["a", "ab", "ac", "z"])

if __name__ == '__main__':
    unittest.main()
