class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # store a set to quickly identify duplicat chars
        # hashset lets us store val -> idx
        #   if we reach a duplicate, we can jump to idx of the char prev
        result = 0
        substring = {} # val -> idx
        left = 0
        for right, char in enumerate(s):
            if char in substring:
                left = max(left, substring[char] + 1)

            result = max(result, right-left+1)
            substring[char] = right

        return result