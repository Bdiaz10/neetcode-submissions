class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreqs = [0] * 26
        tFreqs = [0] * 26

        if len(s) != len(t):
            return False
        
        for char in s:
            sFreqs[ord('a')-ord(char)] += 1
        for char in t:
            tFreqs[ord('a')-ord(char)] += 1
        
        return sFreqs == tFreqs
        