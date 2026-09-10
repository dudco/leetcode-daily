# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def chk(node: TreeNode):
            lsum, llen, lcnt = 0, 0, 0
            rsum, rlen, rcnt = 0, 0, 0
            if node.left is not None:
                lsum, llen, lcnt = chk(node.left)

            if node.right is not None:
                rsum, rlen, rcnt = chk(node.right)

            s = lsum + rsum + node.val
            l = llen + rlen + 1
            c = lcnt + rcnt + (1 if s // l == node.val else 0)
            return s, l, c

        _, _, c = chk(root)
        return c
