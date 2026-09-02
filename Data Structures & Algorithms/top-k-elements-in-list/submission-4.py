class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        vals = []
        for key, val in freqs.items():
            vals.append((val, key))
        
        vals.sort(reverse=True)

        res = []
        for i in range(k):
            res.append(vals[i][1])
        return res
