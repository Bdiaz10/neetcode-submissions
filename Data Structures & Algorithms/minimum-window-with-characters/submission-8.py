class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # trick here is there may be dups in t, so you cant just validate with (if char in t)
        # need to use a freq dict for t
        # use a sliding freq dict window, when the freqs in the window match the freqs of t:
        #   increment the 'have' variable to show you have all the chars you need for one char
        # if the freq in the window drops below the tfreq, decrement the have variable
        tfreqs = {}
        for char in t:
            tfreqs[char] = tfreqs.get(char, 0) + 1
        
        have = 0
        need = len(tfreqs)

        result = ""

        window = {}
        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            
            if char in tfreqs and window[char] == tfreqs[char]:
                have += 1
            
            while have == need:
                windowLength = right - left + 1
                if windowLength < len(result) or not result:
                    result = s[left:right+1]
                
                window[s[left]] -= 1
                if s[left] in tfreqs and window[s[left]] < tfreqs[s[left]]:
                    have -= 1
                left += 1

        return result