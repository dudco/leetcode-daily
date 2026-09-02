import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.smallestNumber("1234", 256), "1488")


if __name__ == '__main__':
    unittest.main()