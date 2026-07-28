class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))

        left = 0
        right = len(s1)-1
        while right < len(s2):
            s = ''.join(sorted(s2[left:right+1]))
            if s == s1:
                return True
            left += 1
            right += 1

        return False
