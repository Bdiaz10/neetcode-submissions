import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        maxheap = []

        for i, n in enumerate(nums):
            heapq.heappush(maxheap, (-n, i))

            
            if i >= k-1:
                while maxheap and  maxheap[0][1] <= i-k:
                    heapq.heappop(maxheap)
                result.append(-maxheap[0][0])
        return result