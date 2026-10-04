class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # parents of each group, initialized to themselves
        parent = [i for i in range(1, len(edges)+1)]

        # find the parent of the node
        # the parent represenet the group or component this node belongs to
        def find(x):
            if parent[x-1] == x:
                return x
            return find(parent[x-1])
        
        def union():
            for u, v in edges:
                uRoot = find(u)
                vRoot = find(v)

                if uRoot == vRoot:
                    return [u, v]
                
                parent[vRoot-1] = uRoot
        
            return []

        return union()
        