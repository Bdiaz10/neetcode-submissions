# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # get result from left
        # add 1
        # pass as current index to right
        result = [0]
        def dfs(node, steps):
            if not node:
                return steps
            left = dfs(node.left, steps)
            steps = left + 1
            if steps == k:
                result[0] = node.val
            right = dfs(node.right, steps)
            return right

        dfs(root, 0)
        return result[0]

        

        