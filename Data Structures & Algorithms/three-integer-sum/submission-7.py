class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, n in enumerate(nums):
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = n + nums[left] + nums[right]
                if total == 0:
                    res.add((n, nums[left], nums[right]))
                    left += 1
                    right -=1
                    
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return list(res)