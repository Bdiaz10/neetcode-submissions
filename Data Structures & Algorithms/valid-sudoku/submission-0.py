from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set) # row index -> {vals}
        colSet = defaultdict(set) # col index -> {vals}
        subBoxSet = defaultdict(set) # sub box id -> {vals}

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                if val in rowSet[row]:
                    return False
                else:
                    rowSet[row].add(val)

                if val in colSet[col]:
                    return False
                else:
                    colSet[col].add(val)

                
                boxId = (row // 3) *3 + (col //3)
                if val in subBoxSet[boxId]:
                    return False
                else:
                    subBoxSet[boxId].add(val)
        
        return True
