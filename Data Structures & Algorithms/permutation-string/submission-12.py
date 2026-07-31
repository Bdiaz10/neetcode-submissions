class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Freqs = {}
        for char in s1:
            s1Freqs[char] = s1Freqs.get(char, 0) +1
        
        left = 0
        window = {}
        for right, char in enumerate(s2):
            if char in s1Freqs:
                window[char] = window.get(char, 0) +1
                while window[char] > s1Freqs[char]:
                    window[s2[left]] -= 1
                    left += 1
                    
                if window == s1Freqs:
                    return True
            else:
                window = {}
                left = right + 1

        return False

        
