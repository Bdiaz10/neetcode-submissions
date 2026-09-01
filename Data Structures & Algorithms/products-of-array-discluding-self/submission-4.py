class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixs = [1]
        prev = nums[0]
        for n in nums[1:]:
            prefixs.append(prev)
            prev *= n
        
        postfixs = [1]
        prev = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            postfixs.append(prev)
            prev *= nums[i]
        postfixs = list(reversed(postfixs))
        
       
        for i in range(len(postfixs)):
            prefixs[i] *= postfixs[i]
        return prefixs

