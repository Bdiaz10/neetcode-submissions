class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i, path):
            if i == len(nums):
                result.append(path[:])
                return
            for j in range(i, len(path)):
                path[i], path[j] = path[j], path[i]
                backtrack(i+1, path)
                path[i], path[j] = path[j], path[i]
        
        backtrack(0, nums[:])
        return result