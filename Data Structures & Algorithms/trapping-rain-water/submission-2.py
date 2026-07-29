class Solution:
    def trap(self, height: List[int]) -> int:
       
        res = 0
        left = 0
        right = len(height)-1

        leftBoundry = height[left]
        rightBoundry = height[right]

        while left < right:
            if leftBoundry < rightBoundry:
                res += leftBoundry - height[left]
                left += 1
                leftBoundry = max(leftBoundry, height[left])
            else:
                res += rightBoundry - height[right]
                right -= 1
                rightBoundry = max(rightBoundry, height[right])
        return res