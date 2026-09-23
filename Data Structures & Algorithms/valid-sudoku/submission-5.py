from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == '.':
                    continue
                
                if (
                    val in rowSet[row] or
                    val in colSet[col] or
                    val in boxSet[(row//3, col//3)]
                ):
                    return False
                
                rowSet[row].add(val)
                colSet[col].add(val)
                boxSet[(row//3, col//3)].add(val)

        return True
                
