class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        def isTree(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not isTree(neighbor, node):
                    return False
            return True

        return isTree(0, -1) and len(visited) == n
