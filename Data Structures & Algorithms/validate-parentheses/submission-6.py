class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for char in s:
            if char in closeToOpen:
                if not stack or stack[-1] != closeToOpen[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
       