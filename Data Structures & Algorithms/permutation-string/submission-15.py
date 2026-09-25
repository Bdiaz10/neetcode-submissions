class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freqs = [0] * 26
        for char in s1:
            s1Freqs[ord(char) - ord("a")] += 1

        left = 0
        for right, char in enumerate(s2):
            s1Freqs[ord(char) - ord("a")] -= 1

            if right >= len(s1) - 1:
                diffs = set(s1Freqs)
                if len(diffs)==1 and 0 in diffs:
                    return True
                s1Freqs[ord(s2[left]) - ord("a")] += 1
                left += 1

        return False
