class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = n * -1
            left = i + 1
            right = len(nums)-1

            while left < right:
                total = nums[left] + nums[right]
                if total < target:
                    left += 1
                elif total > target:
                    right -=1
                else:
                    result.append([n, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return result