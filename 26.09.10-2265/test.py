import unittest
from collections import deque

import solution


class SolutionTests(unittest.TestCase):
    def build_tree(self, elem: list[int]):
        if not elem:
            return None
        
        it = iter(elem)
        val = next(it)

        if val is None:
            return None
        
        root = solution.TreeNode(val)
        q = deque([root])

        for val in it:
            n = q.popleft()
            if val is not None:
                n.left = solution.TreeNode(val)
                q.append(n.left)

            try:
                val = next(it)
            except StopIteration:
                break

            if val is not None:
                n.right = solution.TreeNode(val)
                q.append(n.right)
                

        return root
            

        
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.averageOfSubtree(self.build_tree([4, 8, 5, 0, 1, None, 6])), 5)

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.averageOfSubtree(self.build_tree([1])), 1)

if __name__ == '__main__':
    unittest.main()
