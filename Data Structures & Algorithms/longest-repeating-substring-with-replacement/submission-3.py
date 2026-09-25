class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        window = {}
        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            mostFrequent = max(window.values())
            while ((right - left + 1) - mostFrequent) > k:
                window[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        return result
