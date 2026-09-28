class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        mostFrequent = 0
        result = 0
        left = 0
        for right, n in enumerate(s):
            window[n] = window.get(n, 0) + 1
            mostFrequent = max(mostFrequent, window[n])

            while (right-left+1) - mostFrequent > k:
                window[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        return result
            