class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # vol = min(a, b) * length

        maxVol = 0
        left = 0
        right = len(heights)-1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxVol = max(maxVol, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxVol
    