class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) +1
        
        a = sorted([(val, key) for key, val in freqs.items()], reverse=True)
        print(a)
        return [s[1] for s in a[:k]]