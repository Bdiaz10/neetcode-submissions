class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(n)}
        for x, y in edges:
            adjlist[x].append(y)
            adjlist[y].append(x)
        
        cycle = set()
        def dfs(node, parent):
            if node in cycle:
                return False
            cycle.add(node)
            for dst in adjlist[node]:
                if dst == parent:
                    continue
                if not dfs(dst, node):
                    return False
            return True
        
        return dfs(0, -1) and len(cycle) == n