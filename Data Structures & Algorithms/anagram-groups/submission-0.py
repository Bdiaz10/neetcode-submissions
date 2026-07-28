class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = []
        for i in range(len(strs)):
            sw = sorted(strs[i])
            sorted_strings.append((''.join(sw), i))
        
        sorted_strings = sorted(sorted_strings)

        print(sorted_strings)

        prev = sorted_strings[0][0]
        res = [[strs[sorted_strings[0][1]]]]

        for ss in sorted_strings[1:]:
            if ss[0] == prev:
                res[len(res)-1].append(strs[ss[1]])
            else:
                res.append([strs[ss[1]]])
                prev = ss[0]


        return res