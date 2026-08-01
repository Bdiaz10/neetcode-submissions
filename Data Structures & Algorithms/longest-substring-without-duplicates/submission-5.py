class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        window = {}
        left = 0
        for right, char in enumerate(s):
            window[char] = window.get(char, 0) + 1

            while left < right and window[char] > 1:
                window[s[left]] -= 1
                left += 1
            
            if len(s[left:right+1]) > len(longest):
                longest = s[left:right+1]

        return len(longest)