# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, [])

    def dfs(self, node: TreeNode, parents: list[int]) -> int:
        ret = 0
        if node.left is not None:
            ret += self.dfs(node.left, [*parents, node.val])

        if node.right is not None:
            ret += self.dfs(node.right, [*parents, node.val])

        if all(node.val >= p for p in parents):
            return ret + 1
        return ret