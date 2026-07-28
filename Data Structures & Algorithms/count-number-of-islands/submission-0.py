class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def removeIsland(row, col):
            if row < 0 or col < 0:
                return
            if row >= len(grid) or col >= len(grid[0]):
                return
            if grid[row][col] != "1":
                return
            grid[row][col] = "0"
            removeIsland(row+1, col)
            removeIsland(row-1, col)
            removeIsland(row, col+1)
            removeIsland(row, col-1)

        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islandCount += 1
                    removeIsland(row, col)
        return islandCount