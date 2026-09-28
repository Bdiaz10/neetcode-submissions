from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic decreasing q

        # highest value seen will remain in q[0]
        # while n > q[-1]:
        #   pop from the right, then append. (keep q in decreasing order before appending)

        # store the index, pop values from the left when they are out of range
        q = deque()
        result = []
        for right, n in enumerate(nums):
            
            while q and n > q[-1][0]:
                q.pop()
            
            q.append((n, right))

            while q and q[0][1] < right+1-k:
                q.popleft()

            if right >= k-1:
                result.append(q[0][0])
        
        return result


        