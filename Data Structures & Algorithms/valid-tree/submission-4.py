class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(n)}
        for src, dst in edges:
           adjlist[src].append(dst)
           adjlist[dst].append(src)
        
        path = set()
        def dfs(source, parent=-1):
            if source in path:
                return False
            path.add(source)
            for dst in adjlist[source]:
                if dst == parent:
                    continue
                if not dfs(dst, source):
                    return False
            return True
        return dfs(0) and len(path) == n