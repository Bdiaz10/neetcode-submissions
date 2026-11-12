# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # at each node: 
        #   is p and q in my subtree?
        #   is one in my subtree and I am the other?
        # if both conditions are True, the current node is the LCA
        result = [root]
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left) # is p/q to the left: P | Q | None
            right = dfs(node.right) # is p/q to the right P | Q | None
            if left and right:
                result[0] = node
                return None
            elif left and (node == p or node == q):
                result[0] = node
                return None
            elif right and (node == p or node == q):
                result[0] = node
                return None

            if node == p or node == q:
                return node
            if left:
                return left
            if right:
                return right
            return None
            
            
        
        dfs(root)
        return result[0]

            