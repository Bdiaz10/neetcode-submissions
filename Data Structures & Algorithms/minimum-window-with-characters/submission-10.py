class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # increment have when the window frequency matches tfrequence
        tfreqs = {}
        for char in t:
            tfreqs[char] = tfreqs.get(char, 0) + 1
        
        have = 0
        need = len(tfreqs)

        result = ''
        window = {}
        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in tfreqs and window[char] == tfreqs[char]:
                have += 1
            
            while have == need:
                length = right - left + 1
                if length < len(result) or not result:
                    result = s[left:right+1]
                
                window[s[left]] -= 1
                if s[left] in tfreqs and window[s[left]] < tfreqs[s[left]]:
                    have -= 1
                left += 1
        
        return result