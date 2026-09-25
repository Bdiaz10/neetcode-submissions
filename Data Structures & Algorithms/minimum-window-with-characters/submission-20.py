class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreqs = {}
        for char in t:
            tFreqs[char] = tFreqs.get(char, 0) + 1
        
        have = 0
        need = len(tFreqs)

        window = {}
        res = ''
        left = -1
        for right in range(len(s)):
            if s[right] not in tFreqs:
                continue
            if left == -1:
                left = right

            window[s[right]] = window.get(s[right], 0) + 1

            if window[s[right]] == tFreqs[s[right]]:
                have += 1
            
            while have == need:
                wordLength = right - left +1
                if wordLength < len(res) or not res:
                    res = s[left:right+1]
                
                window[s[left]] -= 1
                if window[s[left]] < tFreqs[s[left]]:
                    have -= 1
                left += 1
                while left <= right and s[left] not in tFreqs:
                    left += 1

                
        return res
        