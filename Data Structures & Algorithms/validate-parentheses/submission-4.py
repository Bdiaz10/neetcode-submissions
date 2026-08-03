class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for char in s:
            if char in lookup:
                if not stack or stack[-1] != lookup[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0


