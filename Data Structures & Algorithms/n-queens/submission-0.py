class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # go row by row, trying a queen at each valid position
        result = []
        board = [["."] * n for _ in range(n)]

        colSet = set()
        posDiagSet = set()
        negDiagSet = set()
        def backtrack(row):

            if row == n:
                result.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if (
                    col not in colSet and
                    (row+col) not in posDiagSet and
                    (row-col) not in negDiagSet
                ):
                    board[row][col] = "Q"
                    colSet.add(col)
                    posDiagSet.add(row+col)
                    negDiagSet.add(row-col)

                    backtrack(row+1)

                    board[row][col] = "."
                    colSet.remove(col)
                    posDiagSet.remove(row+col)
                    negDiagSet.remove(row-col)

        backtrack(0)
        return result