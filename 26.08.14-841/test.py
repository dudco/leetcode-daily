import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.canVisitAllRooms([[1],[2],[3],[]]), True)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]), False)
    

if __name__ == '__main__':
    unittest.main()