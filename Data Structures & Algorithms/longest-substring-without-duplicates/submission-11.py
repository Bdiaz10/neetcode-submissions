class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = 1
        seen = set()
        left = 0
        for right in range(len(s)):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
            else:
                seen.add(s[right])
                res = max(res, len(seen))
        return res