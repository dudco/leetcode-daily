import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]), 4)
    def test_case2(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]]), 2)
    def test_case3(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]]), 4)
    def test_case4(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(2, [[1,5],[2,8],[2,10],[2,2],[1,6],[1,10],[1,1],[2,5],[1,2]]), 0)
    def test_case5(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(1, [[1,5],[1,6],[1,10],[1,1],[1,2]]), 0)
    def test_case6(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(1, [[2,8],[2,10],[2,2],[2,5]]), 0)
    def test_case7(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(2, [[1,6],[1,8],[1,3],[2,3],[1,10],[1,2],[1,5],[2,2],[2,4],[2,10],[1,7],[2,5]]), 1)
    def test_case8(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(1, [[1,6],[1,8],[1,3],[1,10],[1,2],[1,5],[1,7]]), 0)
    def test_case9(self):
        s = Solution()
        self.assertEqual(s.maxNumberOfFamilies(1, [[2,3],[2,2],[2,4],[2,10],[2,5]]), 1)

    

if __name__ == '__main__':
    unittest.main()