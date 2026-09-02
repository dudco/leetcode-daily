import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.mergeAlternately("abc", "pqr"), "apbqcr")
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.mergeAlternately("ab", "pqrs"), "apbqrs")
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.mergeAlternately("abcd", "pq"), "apbqcd")


if __name__ == '__main__':
    unittest.main()