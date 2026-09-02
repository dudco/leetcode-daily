import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.compress(["a","a","b","b","c","c","c"]), 6)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.compress(["a"]), 1)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 4)

    def test_case4(self):
        s = Solution()
        self.assertEqual(s.compress(["a","a","a","b","b","a","a"]), 6)

    

if __name__ == '__main__':
    unittest.main()