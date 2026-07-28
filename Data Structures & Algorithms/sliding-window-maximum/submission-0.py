class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        left = 0
        right = k-1

        while right < len(nums):
            result.append(max(nums[left:right+1]))

            left += 1
            right += 1
        
        return result