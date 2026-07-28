class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freqs = {}
        for char in s1:
            s1freqs[char] = s1freqs.get(char, 0) + 1
        
        window = {}
        left = 0
        right = 0
        while right < len(s2):
            if s2[right] in s1freqs:
                window[s2[right]] = window.get(s2[right], 0) + 1
                while window[s2[right]] > s1freqs[s2[right]] and left < right:
                    window[s2[left]] -= 1
                    left += 1
                if window == s1freqs: return True
                right += 1
            else:
                right += 1
                left = right
                window = {}
        return False
