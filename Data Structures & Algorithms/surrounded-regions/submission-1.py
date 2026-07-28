from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # all borders 'o's cannot be captured
        # all regions that contain a border 'o' cannot be captured
        # bfs from each border 'o', add to a 'safe' set
        # if (r,c) not in safe set, capture
        q = deque()
        for row in range(len(board)):
            if board[row][0] == 'O':
                q.append((row, 0))
            if board[row][len(board[0])-1] == 'O':
                q.append((row, len(board[0])-1))

        for col in range(len(board[0])):
            if board[0][col] == 'O':
                q.append((0, col))
            if board[(len(board)-1)][col] == 'O':
                q.append((len(board)-1, col))
        
        safe = set()
        for r,c in q:
            safe.add((r, c))

        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        print(q)
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for x, y in neighbors:
                    newRow = row + x
                    newCol = col + y
                    if newRow < 0 or newCol < 0:
                        continue
                    if newRow >= len(board) or newCol >= len(board[0]):
                        continue
                    if (newRow, newCol) in safe:
                        continue
                    if board[newRow][newCol] == 'O':
                        safe.add((newRow, newCol))
                        q.append((newRow, newCol))

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in safe:
                    board[row][col] = 'X'
        
