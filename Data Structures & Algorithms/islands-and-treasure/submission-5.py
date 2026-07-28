class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add treasure chest to a q for bfs
        # at each itr, make the grid val the level

        q = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))
        neighbors = [(0,1), (1,0), (-1,0), (0,-1)]
        distance = 1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for nr, nc in neighbors:
                    newRow = nr + row
                    newCol = nc + col
                    if (
                        newRow >= len(grid) or newCol >= len(grid[0]) or 
                        newRow < 0 or newCol < 0 or
                        grid[newRow][newCol] == -1 or 
                        (newRow, newCol) in visited
                    ):
                        continue
                    grid[newRow][newCol] = distance
                    q.append((newRow, newCol))
                    visited.add((newRow, newCol))
            distance += 1
        return grid