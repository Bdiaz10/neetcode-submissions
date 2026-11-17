class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(i, subset):
            if i >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i+1, subset)

            subset.pop()
            curr = nums[i]
            while i < len(nums) and curr == nums[i]:
                i += 1
            backtrack(i, subset)
        backtrack(0, [])
        return result