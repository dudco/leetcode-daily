import unittest

import solution


class SolutionTests(unittest.TestCase):
    def make_node(self, head: list[int], idx=0):
        if idx >= len(head) - 1:
            return solution.ListNode(head[idx])
        _current = solution.ListNode(head[idx])
        _next = self.make_node(head, idx + 1)
        _current.next = _next
        return _current 
    
    def test_case1(self):
        s = solution.Solution()
        head = self.make_node([3,1])
        self.assertEqual(s.nodesBetweenCriticalPoints(head), [-1, -1])

    def test_case2(self):
        s = solution.Solution()
        head = self.make_node([5,3,1,2,5,1,2])
        self.assertEqual(s.nodesBetweenCriticalPoints(head), [1,3])

    def test_case3(self):
        s = solution.Solution()
        head = self.make_node([1,3,2,2,3,2,2,2,7])
        self.assertEqual(s.nodesBetweenCriticalPoints(head), [3,3])

if __name__ == '__main__':
    unittest.main()