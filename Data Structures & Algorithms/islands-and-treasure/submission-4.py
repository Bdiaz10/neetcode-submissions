class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add treasure chest to q
        # bfs, setting the grid val to the min of itself and the iteration
        q = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))
        
        def visit(r, c):
            if (
                r < 0 or c < 0 or
                r >= len(grid) or c >= len(grid[0]) or
                (r, c) in visited or
                grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            q.append((r,c))


        steps = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps
                visit(r+1, c)
                visit(r-1, c)
                visit(r, c+1)
                visit(r, c-1)

            steps += 1
        return steps