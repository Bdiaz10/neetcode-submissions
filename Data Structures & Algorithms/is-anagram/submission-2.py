class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqs = {}
        for i in range(len(s)):
            freqs[s[i]] = freqs.get(s[i], 0) + 1
            freqs[t[i]] = freqs.get(t[i], 0) - 1
        vals = set(freqs.values())
        return vals == {0}


        
    