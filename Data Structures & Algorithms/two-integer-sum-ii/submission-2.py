class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            diff = target - numbers[i]

            left = i +1
            right = len(numbers)-1
            while left <= right:
                middle = (left + right) // 2
                if numbers[middle] == diff:
                    return [i+1, middle+1]
                if numbers[middle] < diff:
                    left = middle +1
                else:
                    right = middle - 1

        return [-1,-1]