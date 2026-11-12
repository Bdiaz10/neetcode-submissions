# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        
        def dfs(node, prevMax):
            if not node:
                return 0
            newMax = max(node.val, prevMax)
            left = dfs(node.left, newMax)
            right = dfs(node.right, newMax)
            good = 0
            if node.val >= prevMax:
                good += 1
            return left + right + good
            
        
        return dfs(root, float('-inf'))

            