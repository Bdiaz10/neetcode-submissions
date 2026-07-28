class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()

        def dfs(i, path, total):
            if i >= len(nums):
                return
            if total > target:
                return
            if total == target:
                results.append(path.copy())
                return

            for j in range(i, len(nums)):
                if nums[j] + total > target:
                    return
                path.append(nums[j])
                dfs(j, path, total + nums[j])
                path.pop()
        
        dfs(0, [], 0)
        return results