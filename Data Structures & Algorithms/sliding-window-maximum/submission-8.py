import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a maxheap to track the current maximum
        # store the value and the index
        # remove all values that are out of bounds from k
        result = []
        maxheap = []

        for i, num in enumerate(nums):
            heapq.heappush(maxheap, (-num, i))

            if i >= k-1:
                # remove invalid
                while maxheap and maxheap[0][1] < i-k+1:
                    heapq.heappop(maxheap)
                
                result.append(-maxheap[0][0])
        return result