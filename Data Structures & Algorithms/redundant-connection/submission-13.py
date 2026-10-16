class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)] # parent[i] is the parent of i
        print(parent)

        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return [x, y]
            
            parent[yRoot] = xRoot
            return []
        
        for x, y in edges:
            result = union(x, y)
            if result:
                return result
        return []
        