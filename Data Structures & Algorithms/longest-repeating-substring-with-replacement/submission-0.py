class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freqs, k=3
        # a: 4
        # b: 1
        # c: 3

        # window is valid if, sum of values (not including most frequent) is <= k
        # windowlength - k <= highestfreq

        freqs = {}
        longest = 0
        left = 0
        maxf = 0
        for right in range(len(s)):
            freqs[s[right]] = freqs.get(s[right], 0) + 1
            maxf = max(maxf, freqs.get(s[right], 0))

            while ((right - left) + 1) - maxf > k:
                freqs[s[left]] -= 1
                left += 1
            longest = max(longest, (right - left) + 1)
        return longest
