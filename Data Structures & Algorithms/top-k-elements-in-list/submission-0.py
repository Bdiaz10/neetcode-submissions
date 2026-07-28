class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get freqs
        freqs = {} # {1: 1, 2: 2, 3: 3}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1


        # sort by frequency
        sorted_freqs = []
        for key, val in freqs.items():
            sorted_freqs.append((val, key))
        sorted_freqs.sort(reverse=True)


        # return [:k]
        res = []
        for f in sorted_freqs[:k]:
            res.append(f[1])
        return res
