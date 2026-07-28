from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # BFS from the pacific border, starting with border elements in q
        # add reachable coordinates to a set
        # track previously visited coordinates
        q = deque()
        reachable = set()
        for col in range(len(heights[0])):
            q.append((0, col))
            reachable.add((0, col))
        for row in range(len(heights)):
            q.append((row, 0))
            reachable.add((row, 0))
        
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for x, y in neighbors:
                    newRow = row + x
                    newCol = col + y
                    if newRow < 0 or newCol < 0:
                        continue
                    if newRow >= len(heights) or newCol >= len(heights[0]):
                        continue
                    if (newRow, newCol) in reachable:
                        continue
                    if heights[row][col] <= heights[newRow][newCol]:
                        q.append((newRow, newCol))
                        reachable.add((newRow, newCol))
        # atlantic
        q = deque()
        reachable2 = set()
        for col in range(len(heights[0])):
            q.append((len(heights)-1, col))
            reachable2.add((len(heights)-1, col))
        for row in range(len(heights)):
            q.append((row, len(heights[0])-1))
            reachable2.add((row, len(heights[0])-1))
        
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for x, y in neighbors:
                    newRow = row + x
                    newCol = col + y
                    if newRow < 0 or newCol < 0:
                        continue
                    if newRow >= len(heights) or newCol >= len(heights[0]):
                        continue
                    if (newRow, newCol) in reachable2:
                        continue
                    if heights[row][col] <= heights[newRow][newCol]:
                        q.append((newRow, newCol))
                        reachable2.add((newRow, newCol))
        

        res = []
        for row, col in reachable:
            if (row, col) in reachable2:
                res.append([row, col])
        return res
        