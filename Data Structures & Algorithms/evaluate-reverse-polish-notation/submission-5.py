from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        # operators = {"+", "-", "*", "/"}
        # stack = []
        # for t in tokens:
        #     if t not in operators:
        #         stack.append(int(t))
        #     else:
        #         b = stack.pop()
        #         a = stack.pop()
        #         val = 0
        #         if t == "+":
        #             val = a + b
        #         elif t == "-":
        #             val = a - b
        #         elif t == "*":
        #             val = a * b
        #         elif t == "/":
        #             val = int(float(a) / b)
        #         stack.append(val)

        # return stack.pop()
        stack = []
        for t in tokens:
            if t == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif t == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif t == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))
            else:
                stack.append(int(t))

        return stack[0]
