class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        freqs = {} # freqs of current window
        longest = 1
        left = 0
        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            while freqs[s[right]] > 1:
                freqs[s[left]] = freqs.get(s[left], 0) -1
                left += 1
            longest = max(longest, (right-left)+1)
        return longest