class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return
        print(height)
        
        leftMax = [height[0]]
        for i in range(1, len(height)):
            leftMax.append(max(height[i], leftMax[i-1]))
        print(leftMax)
        
        rightMax = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            rightMax.insert(0, max(height[i], rightMax[0]))
        print(rightMax)

        total = 0
        for i in range(len(height)):
            total += min(leftMax[i], rightMax[i]) - height[i]

        return total
        

