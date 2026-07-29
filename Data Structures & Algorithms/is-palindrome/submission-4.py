class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        chars = []
        for char in s:
            if char == " ":
                continue
            if char.isalnum():
                chars.append(char.lower())
            
        left = 0
        right = len(chars)-1
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
        
        return True
