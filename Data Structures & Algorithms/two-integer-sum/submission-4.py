class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousLookup = {} # val -> index
        for i, n in enumerate(nums):
            value = target - n
            if value in previousLookup:
                return [previousLookup[value], i]
            previousLookup[n] = i
        return [-1, -1]
        