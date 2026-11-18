class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # explore coords that start with word[0]
        # track the current index of the word, char should mathc word[i]
        def backtrack(i, row, col, visited):
            if (
                row < 0 or col < 0 or
                row >= len(board) or col >= len(board[0]) or 
                (row, col) in visited
            ):
                return False
            if board[row][col] != word[i]:
                return False
            if i == len(word)-1:
                return True
            visited.add((row, col))
            i += 1
            left = backtrack(i, row-1, col, visited)
            right = backtrack(i, row+1, col, visited)
            up = backtrack(i, row, col+1, visited)
            down = backtrack(i, row, col-1, visited)
            res = left or right or up or down
            visited.remove((row, col))
            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if backtrack(0, row, col, set()):
                        return True
        return False                    
            