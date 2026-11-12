# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        targets = []
        def dfs(node):
            if not node:
                return
            if node.val == subRoot.val:
                targets.append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        print([t.val for t in targets])

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
        
        for target in targets:
            if sameTree(target, subRoot):
                return True
        return False