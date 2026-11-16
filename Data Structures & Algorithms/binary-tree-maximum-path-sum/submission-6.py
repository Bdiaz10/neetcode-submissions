# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return the max path you can make including the root and its left or right subtree
        # update response as the max path including the root

        result = [float('-inf')]
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            result[0] = max(result[0], node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return result[0]


        