# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            left = sameTree(a.left, b.left)
            right = sameTree(a.right, b.right)
            return left and right

        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True
            left = dfs(node.left)
            right = dfs(node.right)
            return left or right

        return dfs(root)