class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def removeIsland(row, col):
            if (
                row < 0 or col < 0 or
                row >= len(grid) or col >= len(grid[row]) or
                grid[row][col] != "1"
            ):
                return
            
            grid[row][col] = "0"

            removeIsland(row+1, col)
            removeIsland(row-1, col)
            removeIsland(row, col+1)
            removeIsland(row, col-1)
        

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1":
                    result += 1
                    removeIsland(row, col)
        return result
        