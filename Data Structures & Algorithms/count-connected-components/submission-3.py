class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1
        return result
            