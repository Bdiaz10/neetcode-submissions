class Solution:
    def isValid(self, s: str) -> bool:
        # go through s, if open bracket add to stack
        # if closing bracket, check if match, pop, if not match, return false
        lookup = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
       
        stack = []
        for char in s:
            if char in lookup:
                stack.append(char)
            else:
                if len(stack) > 0 and lookup[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
