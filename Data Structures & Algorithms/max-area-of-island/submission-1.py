class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def getArea(row, col):
            if (
                row < 0 or col < 0 or
                row >= len(grid) or col >= len(grid[0]) or
                grid[row][col] != 1
            ):
                return 0
            
            grid[row][col] = 0
            
            return 1 + (
                getArea(row+1, col) + 
                getArea(row-1, col) + 
                getArea(row, col+1) + 
                getArea(row, col-1) 
            )

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    result = max(result, getArea(row, col))
        return result
        