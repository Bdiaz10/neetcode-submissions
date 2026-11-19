class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # map[number] = [possible letters]

        # "34"
        # i = 0     i = 1
        # [d]   ->  [dg]
        #       ->  [dh]
        #       ->  [di]

        # [e]   ->  [eg]
        #       ->  [eh]
        #       ->  [ei]

        # [f]   ->  [fg]
        #       ->  [fh]
        #       ->  [fi]
        # base case i == len(digits) processes all digits
        # backtrack to explore each candidate
        if not digits:
            return []
        
        number_pad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        result = []
        current = []
        def backtrack(i):
            if i == len(digits):
                result.append(current.copy())
                return
            for char in number_pad[digits[i]]:
                current.append(char)
                backtrack(i+1)
                current.pop()
        backtrack(0)
        return [''.join(r) for r in result]

        
        