import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.missingMultiple([8,2,3,4,6], 2), 10)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.missingMultiple([1,4,7,10,15], 5), 5)

    

if __name__ == '__main__':
    unittest.main()