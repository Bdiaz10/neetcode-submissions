class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        window = {} # val -> index
        left = 0
        for right, n in enumerate(s):
            if n in window:
                left = max(left, window[n]+1)
            result = max(result, right-left+1)
            window[n] = right
        return result