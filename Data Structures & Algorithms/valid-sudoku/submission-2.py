from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        subBoxSet = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                if val == '.':
                    continue
                
                subBoxId = ((row // 3), (col // 3))
            
                if val in rowSet[row] or val in colSet[col] or val in subBoxSet[subBoxId]:
                    return False

                rowSet[row].add(val)
                colSet[col].add(val)
                subBoxSet[subBoxId].add(val)
        return True