class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        longest = 1
        for n in nums:
            if (n-1) not in nums:
                count = 1
                val = n
                while (val+1) in nums:
                    count += 1
                    val += 1 
                longest = max(count, longest)
        return longest
        