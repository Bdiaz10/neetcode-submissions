class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs = {}
        for char in t:
            freqs[char] = freqs.get(char, 0)+1
        
        have = 0
        need = len(freqs)

        res = ""

        window = {}
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in freqs and freqs[s[right]] == window[s[right]]:
                have += 1
            
            while have == need:
                if len(s[left:right+1]) < len(res) or not res:
                    res = s[left:right+1]
                
                window[s[left]] -= 1
                if s[left] in freqs and window[s[left]] < freqs[s[left]]:
                    have -= 1
                left += 1
        
        return res
