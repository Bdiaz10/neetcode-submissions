class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Freqs = [0] * 26
        s2Freqs = [0] * 26
        for i in range(len(s1)):
            s1Freqs[ord(s1[i])-ord('a')] += 1
            s2Freqs[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(len(s1Freqs)):
            if s1Freqs[i] == s2Freqs[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            idx = ord(s2[right])-ord('a')
            s2Freqs[idx] += 1
            if s2Freqs[idx] == s1Freqs[idx]:
                matches += 1
            elif s2Freqs[idx] == s1Freqs[idx] +1:
                matches -= 1
            
            idx = ord(s2[left])-ord('a')
            s2Freqs[idx] -= 1
            if s2Freqs[idx] == s1Freqs[idx]:
                matches += 1
            elif s2Freqs[idx] == s1Freqs[idx]-1:
                matches -= 1
            left += 1
           
            
        return matches == 26
        
        

