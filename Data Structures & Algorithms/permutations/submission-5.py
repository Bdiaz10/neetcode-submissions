class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def backtrack(i, perm):
            if i == len(nums):
                result.append(perm.copy())
                return
            
            for j in range(i, len(perm)):
                perm[i], perm[j] = perm[j], perm[i]
                backtrack(i+1, perm)
                perm[i], perm[j] = perm[j], perm[i]
        
        backtrack(0, nums)
        return result