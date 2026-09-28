class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # store t character freqs

        # store a current window of sFreqs as we iterate
        
        # add each value to the window:
        #   if the windowFrequency matches the tFrequency store
        #       we have 1 value with the correct Frequency count in the window
        #   if the number of matches == key count of tFreqs
        #       the window is valid, record the string
        #       
        #       Try to find smaller substrings by shrinking from the left
        #       if we remove a value, decrement the frequency
        #          if the frequency drops below tFreqs, we lost a match. decrement match
        # stores result string as indexes to avoid string copy

        tFreqs = {}
        for char in t:
            tFreqs[char] = tFreqs.get(char, 0) + 1
        
        have = 0
        need = len(tFreqs)

        result = []

        window = {}
        left = 0
        for right, n in enumerate(s):
            window[n] = window.get(n, 0) + 1

            if n in tFreqs and tFreqs[n] == window[n]:
                have += 1
            
            while have == need:
                # substring = s[left:right+1]
                # if len(substring) < len(result) or not result:
                #     result = substring
                if not result or (right-left+1) < (result[1]-result[0]+1):
                    result = [left, right]
                
                if s[left] in tFreqs and tFreqs[s[left]] == window[s[left]]:
                    have -= 1
                window[s[left]] -= 1
                left += 1

        return s[result[0]: result[1]+1] if result else ""
        
