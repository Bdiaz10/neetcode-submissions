class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {} # val -> idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in lookup:
                return [lookup[diff], i]
            else:
                lookup[n] = i
        return [-1,-1]