class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0

        left = 0 
        right = len(height)-1

        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if leftMax < rightMax:
                result += leftMax - height[left]
                left += 1
                leftMax = max(leftMax, height[left])
            else:
                result += rightMax - height[right]
                right -= 1
                rightMax = max(rightMax, height[right])

        return result