# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #  return a valid subtress min and max value: (1, 3)
    
        
        # verify left subtree:
        # maxValue < root

        # verify right subtree:
        # minValue > root

        def dfs(node):
            if not node:
                return [float('inf'), float('-inf')]
            
            leftMin, leftMax = dfs(node.left)
            rightMin, rightMax = dfs(node.right)

            if leftMax < node.val and rightMin > node.val:
                least = min(leftMin, node.val)
                greatest = max(rightMax, node.val)
                return [least, greatest]

            return [float('-inf'), float('inf')]
        result = dfs(root)
        return result[0] != float('-inf')
