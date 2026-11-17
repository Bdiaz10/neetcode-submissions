class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # decision
        # add open bracket
        # add closed bracket

        # closed cant cant exceed open count
        result = []
        def backtrack(current, openCount, closeCount):
            if openCount == n and closeCount == n:
                result.append(''.join(current.copy()))
                return
            
            if openCount < n:
                current.append("(")
                backtrack(current, openCount+1, closeCount)
                current.pop()

            if closeCount < openCount:
                current.append(")")
                backtrack(current, openCount, closeCount+1)
                current.pop()
            
        
        backtrack([], 0, 0)
        return result
            

           
