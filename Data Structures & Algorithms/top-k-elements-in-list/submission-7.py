class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        groups = [[] for i in range(len(nums) + 1)] 

        for key, val in freqs.items():
            groups[val].append(key)

        res = []
        for i in range(len(groups)-1, -1, -1):
            res.extend(groups[i])
            if len(res) >= k:
                return res
        return res
