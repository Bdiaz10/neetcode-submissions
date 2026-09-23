import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        minheap = [(value, key) for key, value in freqs.items()]
        heapq.heapify(minheap)
        while len(minheap) > k:
            heapq.heappop(minheap)
        return [x[1] for x in minheap]