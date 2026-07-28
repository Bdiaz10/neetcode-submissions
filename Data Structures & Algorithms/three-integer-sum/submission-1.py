class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
                    right -=1
                    continue
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        print(nums)
        return list(res)