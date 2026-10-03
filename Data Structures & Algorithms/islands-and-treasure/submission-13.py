from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add treasure chest to q for bfs
        # at each level, increments steps by 1 ( distnace from treasure )
        
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        neighbors = [(0,1), (1,0), (-1,0), (0,-1)]
        distance = 1
        while q:
            for i in range(len(q)):
                row, col = q.popleft()

                for nr, nc in neighbors:
                    newRow = row + nr
                    newCol = col + nc

                    if (
                        newRow < 0 or newCol < 0 or
                        newRow >= len(grid) or newCol >= len(grid[newRow]) or
                        grid[newRow][newCol] != 2147483647
                    ):
                        continue
                
                    grid[newRow][newCol] = distance
                    q.append((newRow, newCol))
            distance += 1

