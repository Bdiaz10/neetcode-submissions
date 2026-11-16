class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # choices:
        # add value to currentSum
        # dont add value to the currentSum
        result = []
        def backtrack(i, currentPath):
            if i >= len(nums):
                return
            if sum(currentPath) > target:
                return
            if sum(currentPath) == target:
                result.append(currentPath.copy())
                return
            currentPath.append(nums[i])
            backtrack(i, currentPath)

            currentPath.pop()
            backtrack(i+1, currentPath)
        backtrack(0, [])
        return result
        