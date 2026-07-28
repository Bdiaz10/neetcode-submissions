from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add treasure chests to q from BFS
        # check neighbors, if traversable:
        #   change its value to the current iteration, add to q
        visited = set()
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))
        
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for x, y in neighbors:
                    newRow = row + x
                    newCol = col + y
                    if newRow < 0 or newCol < 0: 
                        continue
                    if newRow >= len(grid) or newCol >= len(grid[0]): 
                        continue
                    if (newRow, newCol) in visited:
                        continue
                    if grid[newRow][newCol] != -1 and grid[newRow][newCol] != 0:
                        grid[newRow][newCol] = grid[row][col] + 1
                        q.append((newRow, newCol))
                        visited.add((newRow, newCol))
        
        
    
      

