class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window is valid if
        #   len(window) - highestFrequency <= k
        res = 0
        window = {}
        left = 0
        maxFrequency = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            maxFrequency = max(maxFrequency, window[char])

            while (right-left+1) - maxFrequency > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
