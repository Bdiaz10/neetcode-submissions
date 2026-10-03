from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    freshCount += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        

        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        minute = 0 
        while q and freshCount > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for nr, nc in neighbors:
                    newRow = row + nr
                    newCol = col + nc

                    if (
                        newRow < 0 or newCol < 0 or
                        newRow >= len(grid) or newCol >= len(grid[newRow]) or
                        grid[newRow][newCol] != 1
                    ):
                        continue
                    
                    grid[newRow][newCol] = 2
                    freshCount -= 1
                    q.append((newRow, newCol))

            minute += 1
        
        return minute if freshCount == 0 else -1

        