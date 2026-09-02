import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.removeStars("leet**cod*e"), "lecoe")
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.removeStars("erase*****"), "")
    

if __name__ == '__main__':
    unittest.main()