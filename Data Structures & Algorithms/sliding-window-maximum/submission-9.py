import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a max heap to track the highest value seen
        # store the index as well
        # while the index is outisde of the current window, remove from max heap, not needed
        result = []
        maxheap = []
        for i, n in enumerate(nums):
            heapq.heappush(maxheap, (-n, i))
            if (i+1) >= k:
                while maxheap[0][1] < (i+1-k):
                    heapq.heappop(maxheap)

                result.append(-maxheap[0][0])
        return result