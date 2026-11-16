# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder traversal including None values
        result = []
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        print(data)
        idx = 0
        def buildTree():
            nonlocal idx
            if data[idx] == "N":
                idx += 1
                return
            root = TreeNode(int(data[idx]))
            idx += 1
            root.left = buildTree()
            root.right = buildTree()
            return root
        return buildTree()
        





