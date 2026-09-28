class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) +1
        
        store = [[] for i in range(len(nums)+1)]

        for val, freq in freqs.items():
            store[freq].append(val)
        
        result = []
        for i in range(len(store)-1, -1, -1):
            for v in store[i]:
                if len(result) == k:
                    return result
                result.append(v)
        return result
                 