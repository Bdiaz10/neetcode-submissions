class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        # find the compressed parent of the node (start of the sequence)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])      # Path compression
            return parent[x]

        # join to trees together, rank is used to attach the smaller tree to the bigger tree
        # false if joining trees creates a cycle
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            # same root, this would create a cycle
            if rootX == rootY:
                return False

            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]