class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find target row
        left = 0
        right = len(matrix)-1
        targetRow = -1
        while left <= right:
            middleRow = (right + left) // 2

            # if target in middle row
            if target < matrix[middleRow][0]:
                right = middleRow -1
            elif target > matrix[middleRow][len(matrix[middleRow])-1]:
                left = middleRow + 1
            else:
                targetRow = middleRow
                break

        if targetRow == -1:
            return False

        # binary search on target row
        left = 0
        right = len(matrix[targetRow])-1
        while left <= right:
            middle = (left + right) // 2
            if target == matrix[targetRow][middle]:
                return True
            elif target < matrix[targetRow][middle]:
                right = middle -1
            else:
                left = middle +1
        
        return False