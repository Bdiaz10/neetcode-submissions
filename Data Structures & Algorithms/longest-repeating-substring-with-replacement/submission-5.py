class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        window = {}
        highestFreq = 0
        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            highestFreq = max(highestFreq, window[char])
            while ((right - left + 1) - highestFreq) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            result = max(result, right-left+1)
        return result
