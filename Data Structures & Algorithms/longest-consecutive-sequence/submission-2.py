class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        res = 0
        for n in nums:
            # if start of sequence
            if (n-1) not in numset:
                currentCount = 1
                val = n
                while val+1 in numset:
                    currentCount += 1
                    val += 1
                res = max(res, currentCount)
                
        return res