# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        deepest = [0]
        def dfs(node, level):
            if not node:
                return None
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            if not left and not right:
                deepest[0] = max(deepest[0], level)
            return node
        if root:
            dfs(root, 1)
            return deepest[0]
        else:
            return 0
