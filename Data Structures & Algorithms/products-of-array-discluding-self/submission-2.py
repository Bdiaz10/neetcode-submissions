class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1]
        prev = nums[0]
        for n in nums[1:]:
            leftProducts.append(prev)
            prev *= n
        print(leftProducts)

        rightProducts = [1]
        prev = nums[-1]
        for n in reversed(nums[:len(nums)-1]):
            rightProducts.insert(0, prev)
            prev *= n
        
        res = []
        for i in range(len(nums)):
            res.append(rightProducts[i] * leftProducts[i])
        return res