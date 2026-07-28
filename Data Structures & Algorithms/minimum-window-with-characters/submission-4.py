class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tfreqs = {}
        for char in t:
            tfreqs[char] = tfreqs.get(char, 0) +1

        have = 0
        need = len(tfreqs)

        res = [-1, -1]
        length = float('inf')

        window = {}
        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            if char in tfreqs and window[char] == tfreqs[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < length:
                    res = [left, right]
                    length = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in tfreqs and window[s[left]] < tfreqs[s[left]]:
                    have -= 1
                left += 1 
        l, r = res
        return s[l : r + 1] if length != float("inf") else ""
