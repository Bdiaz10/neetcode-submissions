import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [(weight * -1) for weight in stones]
        heapq.heapify(heap)

        # heap is a tree like structure allowing for easy sorted traversal
        # min heap by default
        # log n add/remove
        
        # min heap fix: *-1 on insert and removal
        while len(heap) > 1:
            y = heapq.heappop(heap) * -1
            x = heapq.heappop(heap) * -1

            if x < y:
                y = y-x
                heapq.heappush(heap, (y * -1))
        
        return (heap[0] * -1) if len(heap) > 0 else 0
            