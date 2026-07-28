class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        # make adj list
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        # dfs to add connected to a visited
        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adjList[node]:
                dfs(neighbor)
            
        
        count = 0
        for node in adjList:
            if node not in visited:
                count += 1
                dfs(node)
        return count
            