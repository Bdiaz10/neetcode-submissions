class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # choices:
        # add value to currentSum
        # dont add value to the currentSum
        result = []
        def backtrack(i, currentPath, currentSum):
            if i >= len(nums) or currentSum > target:
                return
            
            if currentSum == target:
                result.append(currentPath.copy())
                return
            currentPath.append(nums[i])
            backtrack(i, currentPath, currentSum + nums[i])

            currentPath.pop()
            backtrack(i+1, currentPath, currentSum)

        backtrack(0, [], 0)
        return result
        