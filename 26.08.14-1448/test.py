import unittest
from collections import deque

from solution import Solution, TreeNode


def build_tree_from_list(vals):
    if not vals:
        return None
    it = iter(vals)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for val in it:
        node = q.popleft()
        # left child
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        # right child (advance iterator)
        try:
            val = next(it)
        except StopIteration:
            break
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root

class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        vals = [3, 1, 4, 3, None, 1, 5]
        root = build_tree_from_list(vals)
        self.assertEqual(s.goodNodes(root), 4)
    def test_case2(self):
        s = Solution()
        vals = [3,3,None,4,2]
        root = build_tree_from_list(vals)
        self.assertEqual(s.goodNodes(root), 3)
    

if __name__ == '__main__':
    unittest.main()