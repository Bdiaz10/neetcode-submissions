class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        substring = set()
        left = 0
        for right, n in enumerate(s):
            while n in substring:
                substring.remove(s[left])
                left += 1
            substring.add(n)
            result = max(result, len(substring))
        return result