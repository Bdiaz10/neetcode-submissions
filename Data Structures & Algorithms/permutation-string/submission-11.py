class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def getFreqs(s):
            freqs = {}
            for char in s:
                freqs[char] = freqs.get(char, 0) +1
            return freqs

        sFreqs = getFreqs(s1)

        for right in range(len(s2)-len(s1)+1):
            if s2[right] in sFreqs:
                s2Freqs = getFreqs(s2[right:right+len(s1)])
                if sFreqs == s2Freqs:
                    return True
        
        
        return False

            