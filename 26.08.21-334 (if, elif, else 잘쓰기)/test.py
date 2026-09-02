import unittest

from solution import Solution


class SolutionTests(unittest.TestCase):
    # def test_case1(self):
    #     s = Solution()
    #     self.assertEqual(s.increasingTriplet([1,2,3,4,5]), True)
    # def test_case2(self):
    #     s = Solution()
    #     self.assertEqual(s.increasingTriplet([5,4,3,2,1]), False)
    # def test_case3(self):
    #     s = Solution()
    #     self.assertEqual(s.increasingTriplet([2,1,5,0,4,6]), True)
    # def test_case4(self):
    #         s = Solution()
    #         self.assertEqual(s.increasingTriplet([5,0,1,2,4,3]), True)
    def test_case5(self):
            s = Solution()
            self.assertEqual(s.increasingTriplet([1,5,0,4,1,3]), True)
    

    

if __name__ == '__main__':
    unittest.main()