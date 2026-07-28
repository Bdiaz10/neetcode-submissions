class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def calculateArea(row, col):
            if row < 0 or col < 0:
                return 0
            if row >= len(grid) or col >= len(grid[row]):
                return 0
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            return 1 + (
                calculateArea(row+1, col) +
                calculateArea(row-1, col) +
                calculateArea(row, col+1) +
                calculateArea(row, col-1)
            )
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, calculateArea(row, col))
        return maxArea