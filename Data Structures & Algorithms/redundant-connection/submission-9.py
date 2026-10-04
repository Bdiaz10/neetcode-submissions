class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # parent[i] = the root of the group

        # initialize each parent to itself
        parent = [i for i in range(1, len(edges)+1)]

        # find the group that n belongs to
        def find(n):
            if parent[n-1] != n:
                return find(parent[n-1])
            return n
        
        for u, v in edges:
            uRoot = find(u)
            vRoot = find(v)

            if uRoot == vRoot:
                return [u, v]
            
            parent[vRoot-1] = uRoot
