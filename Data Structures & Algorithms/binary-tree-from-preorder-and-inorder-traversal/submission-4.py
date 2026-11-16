# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre order gives us the root
        # idx of root inorder partitions to left and right subtrees

        # recursivly pass left and right borders
        idxLookup = {val: i for i, val in enumerate(inorder)}

        rootIdx = 0
        def dfs(left, right):
            nonlocal rootIdx
            if left > right:
                return None

            root = TreeNode(preorder[rootIdx])
            rootIdx += 1

            partition = idxLookup[root.val]
            root.left = dfs(left, partition-1)
            root.right = dfs(partition+1, right)
            return root
        
        return dfs(0,len(inorder)-1)
