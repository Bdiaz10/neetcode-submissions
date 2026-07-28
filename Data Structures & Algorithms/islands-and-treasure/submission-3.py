class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        def addSquare(row, col):
            if (
                row < 0 or col < 0 or
                row == len(grid) or col == len(grid[0]) or
                (row,col) in visited or
                grid[row][col] == -1
            ):
                return
            
            q.append((row, col))
            visited.add((row,col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row,col))
                    visited.add((row,col))
        
        distance = 0
        while q:

            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addSquare(r+1, c)
                addSquare(r-1, c)
                addSquare(r, c+1)
                addSquare(r, c-1)

            distance += 1
        return distance

