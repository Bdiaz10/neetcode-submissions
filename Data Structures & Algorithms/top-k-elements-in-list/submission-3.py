class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        res = []
        for num, freq in freqs.items():
            res.append((freq, num))
        
        res.sort(reverse=True)

        output = []
        for i in range(k):
            output.append(res[i][1])
        return output
