class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring = {} # val -> idx
        left = 0
        for right, n in enumerate(s):
            if n in substring:
                left = max( substring[n] + 1, left)
            
            substring[n] = right
            result = max(result, right - left+1)
        return result