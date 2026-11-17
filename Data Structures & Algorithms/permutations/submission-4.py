class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        result = []
        permutations = self.permute(nums[1:])
        for perm in permutations:
            for i in range(len(perm)+1):
                cpy = perm.copy()
                cpy.insert(i, nums[0])
                result.append(cpy.copy())
        return result