class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFreqs = {}
        for char in s:
            sFreqs[char] = sFreqs.get(char, 0) + 1
        
        for char in t:
            if char not in sFreqs or sFreqs[char] == 0:
                return False
            sFreqs[char] -= 1
        
        vals = list(set(sFreqs.values()))
        return len(vals) == 0 or (len(vals) == 1 and vals[0] == 0)