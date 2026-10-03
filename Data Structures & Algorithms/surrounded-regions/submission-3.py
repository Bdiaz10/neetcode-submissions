from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # bfs from each border O and mark islands as safe

        # remove all Os not marked as safe
        q = deque()
        for row in range(len(board)):
            if board[row][0] == "O":
                q.append((row, 0))
            if board[row][len(board[0])-1] == "O":
                q.append((row, len(board[0])-1))

        for col in range(len(board[0])):
            if board[0][col] == "O":
                q.append((0, col))
            if board[len(board)-1][col] == "O":
                q.append((len(board)-1, col))

        
        safe = set()
        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                safe.add((row, col))
                for nr, nc in neighbors:
                    newRow = row + nr
                    newCol = col + nc

                    if (
                        newRow < 0 or newCol < 0 or
                        newRow >= len(board) or newCol >= len(board[newRow]) or
                        (newRow, newCol) in safe or 
                        board[newRow][newCol] == "X"
                    ):
                        continue
                    
                    q.append((newRow, newCol))
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in safe:
                    board[row][col] = "X"


        