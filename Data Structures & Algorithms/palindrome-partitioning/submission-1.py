class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        palindromes = []

        def backtrack(candidates):
            if len(candidates) == 0:
                result.append(palindromes.copy())
                return
            
            for i in range(1, len(candidates)+1):
                candidate = candidates[:i]
                if candidate == candidate[::-1]:
                    palindromes.append(candidate)
                    backtrack(candidates[i:])
                    palindromes.pop()
        
        backtrack(s)
        return result