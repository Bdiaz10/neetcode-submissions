class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i+1 for i in range(len(edges))]
        def find(x):
            if parent[x-1] == x:
                return x
            return find(parent[x-1])
        
        for x, y in edges:
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return [x, y]
            
            parent[yRoot-1] = xRoot
        
        return []
