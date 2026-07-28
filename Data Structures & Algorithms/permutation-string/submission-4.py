class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freqs = [0] * 26
        for char in s1:
            s1freqs[ord(char)-ord('a')] += 1
        
        subfreqs = [0] * 26
        left = 0
        right = 0
        while right < len(s2):
            if s1freqs[ord(s2[right])-ord('a')] > 0:
                subfreqs[ord(s2[right])-ord('a')] += 1
                while subfreqs[ord(s2[right])-ord('a')] > s1freqs[ord(s2[right])-ord('a')] and left < right:
                    subfreqs[ord(s2[left])-ord('a')] -= 1
                    left += 1
                if subfreqs == s1freqs:
                    return True
                right += 1
            else:
                subfreqs = [0] * 26
                right += 1
                left = right
                

        return False

                
