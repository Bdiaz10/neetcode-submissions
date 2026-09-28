class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add (val, idx) to stack
        # when n is more than stack[-1]:
        # pop from stack, calculate idx and update result array
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                tmp, idx = stack.pop()
                result[idx] = i - idx
            stack.append((t, i))
        return result