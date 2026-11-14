# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traversing through a BST inorder wil go from least to greatest
        # global counter tracks steps
        steps = [0]
        result = [0]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            steps[0] += 1
            if steps[0] == k:
                result[0] = node.val
            dfs(node.right)
        dfs(root)
        return result[0]


        