from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            lookup[key].append(word)
        
        return list(lookup.values())
            