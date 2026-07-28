class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # sw -> og words
        for word in strs:
            sw = sorted(word)
            sw = ''.join(sw)
            if sw not in groups.keys():
                groups[sw] = [word]
            else:
                groups[sw].append(word)
        
        return list(groups.values())