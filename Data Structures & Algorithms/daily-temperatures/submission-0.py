class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # add (val, idx) to stack

        # while val is more than stack[-1]
            # pop from stack, add counter to indx

        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                idx, val = stack.pop()
                res[idx] = i - idx

            stack.append((i, t))
        
        return res
