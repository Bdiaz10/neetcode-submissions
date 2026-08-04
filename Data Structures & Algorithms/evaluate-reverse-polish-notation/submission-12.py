import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                flag = False
                if a < 0 and b < 0:
                    a = a * -1
                    b = b *-1
                elif b < 0:
                    b = b * -1
                    flag = True
                elif a < 0:
                    a = a * -1
                    flag = True
                res = a // b
                if flag:
                    res *= -1
                stack.append(res)
            else:
                stack.append(int(token))
       
        return stack[-1]