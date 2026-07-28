class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if righ pointer is more that mid
            # all vals to the right don't need to be proccessed
            # right = mid - 1
        # else
            # investivate to the right
            # left = mid + 1
        left = 0
        right = len(nums)-1
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[right] > nums[mid]:
                right = mid -1
            else:
                left = mid + 1
        
        return res