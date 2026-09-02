class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None: return 0
        return self.find_depth(root, 1)

    def find_depth(self, node: TreeNode | None, depth: int):
        if node is None or (node.left is None and node.right is None):
            return depth
        return max(
            self.find_depth(node.left, depth+1),
            self.find_depth(node.right, depth+1),
        )
