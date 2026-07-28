class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        current = []

        def backtrack(start):
            if start >= len(nums) or sum(current) >= target:
                if sum(current) == target:
                    res.append(current.copy())
                return
            
            current.append(nums[start])
            backtrack(start)

            current.pop()
            backtrack(start+1)
        
        backtrack(0)
        return res
            
            