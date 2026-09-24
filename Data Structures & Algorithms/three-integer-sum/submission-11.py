class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        i = 0
        while i < len(nums):
            target = nums[i] * -1
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
            i += 1
        return list(set(res))
            
        