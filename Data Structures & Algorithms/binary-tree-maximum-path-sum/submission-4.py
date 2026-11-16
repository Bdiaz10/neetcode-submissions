# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # compare:
            # maxpath of left subtree
            # maxpath of right subtree
            # combine paths through the root node

        # propogate max path sum from node

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


            

