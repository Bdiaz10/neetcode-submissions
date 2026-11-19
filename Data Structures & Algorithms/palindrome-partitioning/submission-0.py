class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # check all possible subsets, starting at i

        # a -> b -> c

        # start = 0
        # aa -> b



        # aab -> x

        result = []
        palindromes = []
        def backtrack(start):
            if start == len(s):
                result.append(palindromes.copy())
                return
            
            for end in range(start, len(s)):
                substring = s[start:end+1]

                if substring != substring[::-1]:
                    continue
                
                palindromes.append(substring)
                backtrack(end+1)
                palindromes.pop()

        backtrack(0)
        return result

