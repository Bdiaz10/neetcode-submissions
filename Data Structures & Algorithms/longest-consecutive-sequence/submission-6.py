class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in numset:
            if n-1 not in numset:
                count = 0
                val = n
                while val in numset:
                    count += 1
                    val += 1
                res = max(res, count)
        return res
        