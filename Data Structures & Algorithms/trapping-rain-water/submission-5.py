class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) -1

        leftWall = height[left]
        rightWall = height[right]

        result = 0

        while left < right:
            if leftWall < rightWall:
                result += leftWall - height[left]
                left += 1
                leftWall = max(leftWall, height[left])
            else:
                result += rightWall - height[right]
                right -= 1
                rightWall = max(rightWall, height[right])

        return result
