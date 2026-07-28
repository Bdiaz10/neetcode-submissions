class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # invalid window: windowlength - mostfrequent > k
        freqs = {}
        longest = 0
        left = 0
        mostFrequent = 0
        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            mostFrequent = max(mostFrequent, freqs[s[right]])
            while ((right - left) + 1 - mostFrequent) > k:
                freqs[s[left]] -= 1
                left += 1
            longest = max(longest, (right-left)+1)
        return longest