class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # pop from stack and calulate area when you can no longer expand to the right
        stack = []
        result = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                result = max(result, (i - idx) * height)
                start = idx
            stack.append((start, h))
        

        for i, h in stack:
            result = max(result, h * (len(heights)-i))

        return result