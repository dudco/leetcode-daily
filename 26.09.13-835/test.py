import unittest

import solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]), 3)

    # def test_case2(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap([[1]], [[1]]), 1)

    # def test_case3(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap([[0]], [[0]]), 0)

    # def test_case4(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap([[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]]), 1)

    # def test_case5(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap([[1,0],[0,0]], [[0,1],[1,0]]), 1)
    
    # def test_case6(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap([[1,1,1,1],[1,1,0,1],[1,1,1,0],[0,1,0,1]], [[1,1,1,0],[1,1,1,1],[1,1,1,0],[1,0,0,0]]), 9)

    # def test_case7(self):
    #     s = solution.Solution()
    #     self.assertEqual(s.largestOverlap(
    #         [[1,0,1,1,0,1,0,0,1,1],[1,1,1,0,1,1,1,1,1,1],[1,1,1,0,1,1,1,1,1,1],[1,1,1,0,1,1,1,1,1,1],[1,1,1,1,0,1,0,0,1,0],[1,1,1,1,1,1,1,1,0,0],[1,0,1,1,0,1,1,0,0,1],[1,0,1,0,1,1,1,1,1,1],[1,1,1,1,1,0,0,1,1,0],[1,1,0,1,1,0,1,0,1,1]],
    #         [[1,1,0,1,1,1,1,1,1,1],[1,0,0,0,0,1,0,1,1,0],[1,1,1,1,0,1,1,1,1,1],[1,0,0,1,1,1,1,1,0,1],[1,1,1,1,1,0,1,1,0,0],[1,1,1,1,0,1,0,1,1,1],[0,1,1,1,1,0,1,1,1,1],[1,0,1,1,1,0,1,1,0,1],[1,0,1,1,1,0,1,0,0,0],[1,1,1,1,1,1,1,0,1,0]]
    #     ), 53)

    def test_case8(self):
        s = solution.Solution()
        self.assertEqual(s.largestOverlap(
            [[0,0,0,0,0],[0,0,0,1,0],[0,0,0,1,0],[0,1,1,0,0],[0,0,0,1,0]],
            [[0,0,0,1,0],[0,0,0,0,0],[1,1,1,0,1],[0,0,1,1,1],[0,1,0,0,0]]
        ), 4)

if __name__ == '__main__':
    unittest.main()
