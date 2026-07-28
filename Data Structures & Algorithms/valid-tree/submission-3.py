class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = defaultdict(list)
        for frm, t in edges:
            tree[frm].append(t)
            tree[t].append(frm)
        
        cycle = set()
        def dfs(node, prev):
            if node in cycle:
                return False
            
            cycle.add(node)
            for child in tree[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False
            return True
        return dfs(0, -1) and n == len(cycle)