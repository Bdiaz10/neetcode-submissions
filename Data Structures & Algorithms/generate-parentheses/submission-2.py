class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n pairs = n open parens, n closed parens
        # tack open count and close count as we add
        # Decision: TRY BOTH
        # append an open paren
        # append a closed parent
        # constrains:
        # - only add open if openCount < n
        # - only add close if closeCount < openCount
        # base case:
        # opencount == n and closecount == n
        # "(" -> "((" -> "(((" -> "((()"
        #                      -> /
        #             -> "(()" -> "(()("
        #                      -> "(())"
        #     -> "()"
        # ""

        #

        result = []
        def backtrack(currentPath, openCount, closedCount):
            if openCount == n and closedCount == n:
                result.append(''.join(currentPath))
                return
            
            if openCount < n:
                currentPath.append("(")
                backtrack(currentPath, openCount +1, closedCount)
                currentPath.pop()
            
            if closedCount < openCount:
                currentPath.append(")")
                backtrack(currentPath, openCount, closedCount+1)
                currentPath.pop()
        
        backtrack([], 0, 0)
        return result
        