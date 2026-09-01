class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in nums:
            if (n-1) not in numset:
                count = 1
                val = n
                while (val+1) in numset:
                    count += 1
                    val += 1
                res = max(res, count)
        return res