class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort for searching and easy deduplication
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = nums[i] * -1
            left = i +1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -=1
                else:
                    left += 1
        return list(res)
        
