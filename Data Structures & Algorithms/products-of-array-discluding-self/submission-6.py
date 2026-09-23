class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixs = []
        prev = 1
        for n in nums:
            prefixs.append(prev)
            prev *= n
        #print(prefixs)

        postfixs = []
        prev = 1
        for i in range(len(nums)-1,-1,-1):
            postfixs.append(prev)
            prev *= nums[i]
        postfixs.reverse()
        #print(postfixs)

        result = []
        for i in range(len(prefixs)):
            result.append(prefixs[i] * postfixs[i])
        #print(result)
        return result

