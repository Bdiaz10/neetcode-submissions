class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid +1
            elif nums[mid] < nums[right]:
                right = mid

                if mid == 0 or nums[mid] < nums[mid-1]:
                    return nums[mid]
            
        return nums[right]
            
           


        