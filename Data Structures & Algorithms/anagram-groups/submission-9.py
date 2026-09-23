from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list) # (char freq array) -> [anagrams]
        for word in strs:
            freqs = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                freqs[idx] += 1
            key = tuple(freqs)
            lookup[key].append(word)
        return list(lookup.values())