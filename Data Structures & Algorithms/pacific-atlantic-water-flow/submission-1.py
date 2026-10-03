from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # set of coords that pacific can reach
        pacificQ = deque()
        for row in range(len(heights)):
            pacificQ.append((row, 0))
        for col in range(len(heights[0])):
            pacificQ.append((0, col))
        
        # set of coords that atlantic can reach
        atlanticQ = deque()
        for row in range(len(heights)):
            atlanticQ.append((row, len(heights[0])-1))
        for col in range(len(heights[0])):
            atlanticQ.append((len(heights)-1, col))
        
        def bfs(q) -> set:
            neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
            visited = set()
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    visited.add((row, col))

                    for nr, nc in neighbors:
                        newRow = row + nr
                        newCol = col + nc

                        if (
                            newRow < 0 or newCol < 0 or
                            newRow >= len(heights) or newCol >= len(heights[newRow]) or 
                            (newRow, newCol) in visited or
                            heights[newRow][newCol] < heights[row][col]
                        ):
                            continue
                        
                        q.append((newRow, newCol))
            return visited
        
        pacificSet = bfs(pacificQ)
        atlanticSet = bfs(atlanticQ)

        result = []
        for r, c in pacificSet:
            if (r, c) in atlanticSet:
                result.append([r, c])
        return result

        