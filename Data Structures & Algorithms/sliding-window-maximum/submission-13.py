from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        q = deque()
        for right in range(len(nums)):
            while q and q[-1][0] < nums[right]:
                q.pop()
            
            q.append((nums[right], right))

            while q and q[0][1] < right+1 - k:
                q.popleft()
            
            if right >= k-1:
                result.append(q[0][0])
        return result