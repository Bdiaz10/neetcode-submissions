class Solution:
    # prepend each word with len(word)&
    # the '&' tells us we reached the end of out prepended text

    # start from idx 0, process the word, move len(word)
    symbol: str

    def __init__(self):
        self.symbol = '&'

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(f'{len(word)}{self.symbol}{word}')
        r = ''.join(result)
        print(r)
        return r


    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        right = 0
        while right < len(s):
            if s[right] == self.symbol:
                wordLength = int(s[left:right])
                result.append(s[right+1:right+wordLength+1])
                right = right+wordLength+1
                left = right
            else:
                right += 1
        return result