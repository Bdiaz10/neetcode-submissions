class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(str(len(word)))
            result.append('#')
            result.append(word)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while left < len(s):
            right = left
            while s[right] != '#':
                right += 1
            length = int(s[left:right])
            res.append(s[right+1:right+1+length])
            left = right + 1 + length
        
        return res


