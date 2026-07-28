class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        rank = [1 for i in range(len(edges)+1)]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            xRoot = find(x)
            yRoot = find(y)

            if xRoot == yRoot:
                return False
            
            if rank[xRoot] < rank[yRoot]:
                parents[xRoot] = yRoot
            elif rank[xRoot] > rank[yRoot]:
                parents[yRoot] = xRoot
            else:
                parents[yRoot] = xRoot
                rank[xRoot] += 1
            return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]
