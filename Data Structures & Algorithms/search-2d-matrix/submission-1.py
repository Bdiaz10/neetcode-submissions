class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search for the row
        top = 0
        bottom = len(matrix)-1
        targetRow = -1
        while top <= bottom:
            middleRow = top + ((bottom - top) // 2)

            if target < matrix[middleRow][0]:
                bottom = middleRow -1
            elif target > matrix[middleRow][-1]:
                top = middleRow + 1
            else:
                targetRow = middleRow
                break
        
        if targetRow == -1:
            return False
        
        left = 0
        right = len(matrix[targetRow])-1
        while left <= right:
            mid = left + ((right-left) // 2)
            if target < matrix[targetRow][mid]:
                right = mid -1
            elif target > matrix[targetRow][mid]:
                left = mid + 1
            elif matrix[targetRow][mid] == target:
                return True
        
        return False
