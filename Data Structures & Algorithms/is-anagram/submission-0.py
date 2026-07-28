class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if s == t:
            return True
        
        counts = {}
        for i in range(len(s)):
            sChar = s[i]
            counts[sChar] = counts.get(sChar, 0) + 1

            tChar = t[i]
            counts[tChar] = counts.get(tChar, 0) -1
        
        vals = counts.values()
        return set(vals) == {0}

