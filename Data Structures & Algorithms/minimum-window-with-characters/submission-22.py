class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tFreqs = {}
        for char in t:
            tFreqs[char] = tFreqs.get(char, 0) +1
        
        have = 0
        need = len(tFreqs)
        
        result = []
        window = {}
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in tFreqs and window[s[right]] == tFreqs[s[right]]:
                have += 1
            
            while have == need:
                wordLength = right+1-left
                if not result or wordLength < result[1]+1-result[0]:
                    result = [left, right]
                
                window[s[left]] -= 1
                if s[left] in tFreqs and window[s[left]] < tFreqs[s[left]]:
                    have -= 1
                left += 1

        if result:
            return s[result[0]:result[1]+1]
        else:
            return ''

        