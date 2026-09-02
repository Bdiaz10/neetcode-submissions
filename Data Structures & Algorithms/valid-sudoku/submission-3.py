from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subBoxSet = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue
                
                val = board[row][col]
                if val in rowSet[row]:
                    return False
                rowSet[row].add(val)

                if val in colSet[col]:
                    return False
                colSet[col].add(val)

                if val in subBoxSet[(row//3, col//3)]:
                    return False
                subBoxSet[(row//3, col//3)].add(val)
        
        return True
