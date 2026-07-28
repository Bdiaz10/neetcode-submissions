class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs, add all chest to q
        q = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))
        
        distance = 1
        neighbors = [[0,1], [1,0], [0,-1], [-1,0]]

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for nRow, nCol in neighbors:
                    newRow = nRow + row
                    newCol = nCol + col
                    if (
                        newRow < 0 or newCol < 0 or
                        newRow >= len(grid) or newCol >= len(grid[0]) or
                        grid[newRow][newCol] == -1 or
                        (newRow, newCol) in visited

                    ):
                        continue

                    grid[newRow][newCol] = distance
                    q.append([newRow, newCol])
                    visited.add((newRow, newCol))
            distance += 1
        return grid


