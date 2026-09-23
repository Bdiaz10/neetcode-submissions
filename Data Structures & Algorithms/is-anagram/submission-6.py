class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqs = {}
        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
        
        for char in t:
            if char not in freqs:
                return False
            freqs[char] -= 1
            if freqs[char] == 0:
                del freqs[char]
        
        return len(freqs) == 0
        