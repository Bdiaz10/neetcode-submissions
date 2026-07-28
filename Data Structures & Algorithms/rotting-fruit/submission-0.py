from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # store the total number of fresh fruit
        # add the rotten fruit to a q for BFS
        # on each iteration, add neighbors to q and count them as rotten by decrementing fresh
        # the number of iterations for fresh == 0 is the minutes taken
        # if bfs finishes but fresh > 0, impossible to reach final state
        fresh = 0
        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minutes = 0
        while q and fresh > 0:
            # pop from q
            # check each neighbor:
            #   if neighbor is fresh, make it rotten (decrement fresh count, add to q)
            for i in range(len(q)):
                row, col = q.popleft()
                for nr, nc in neighbors:
                    newRow = row + nr
                    newCol = col + nc
                    if newRow < 0 or newCol < 0:
                        continue
                    if newRow >= len(grid) or newCol >= len(grid[0]):
                        continue
                    if grid[newRow][newCol] == 1:
                        fresh -= 1
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
            minutes += 1
        return minutes if fresh == 0 else -1

                