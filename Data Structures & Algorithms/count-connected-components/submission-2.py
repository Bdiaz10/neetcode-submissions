class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # go from 0 - n
        # call dfs on a node, add all vals to set
        # if val in set, return 0 immediately
        # else return 1
        adjlist = {i: [] for i in range(n)}
        for src, dst in edges:
            adjlist[src].append(dst)
            adjlist[dst].append(src)
        
        visited = set()
        def dfs(source):
            if source in visited:
                return 0
            visited.add(source)
            for node in adjlist[source]:
                dfs(node)
            return 1

        result = 0
        for node in adjlist.keys():
            result += dfs(node)
        return result