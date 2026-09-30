class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        targetRow = None
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top =  mid + 1
            else:
                targetRow = mid
                break
        
        if targetRow == None:
            return False
        
        left = 0
        right = len(matrix[targetRow])-1
        while left <= right:
            mid = left + (right - left) // 2
            if target < matrix[targetRow][mid]:
                right = mid - 1 
            elif target > matrix[targetRow][mid]:
                left = mid + 1
            else:
                return True
        
        return False
