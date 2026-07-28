class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1]
        prev = nums[0]
        for n in nums[1:]:
            leftProducts.append(prev)
            prev = prev * n

        rightProducts = [1]
        prev = nums[-1]
        for n in reversed(nums[:len(nums)-1]):
            rightProducts.insert(0, prev)
            prev = prev * n
        
        print(leftProducts)
        # [0, 1, 2, 8]
        print(rightProducts)
        # [48, 24, 6, 0]

        res = []
        for i in range(0, len(nums)):
            res.append(leftProducts[i] * rightProducts[i])

        return res