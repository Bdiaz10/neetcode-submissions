class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        window = set()
        left = 0
        for right, char in enumerate(s):

            while left < right and char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            
            if len(s[left:right+1]) > len(longest):
                longest = s[left:right+1]

        return len(longest)