class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def canFinish(rate: int) -> bool:
            time = 0
            for p in piles:
                time += math.ceil(p / rate)
            return time <= h
        
        left = 1
        right = max(piles)
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                result = mid
                right = mid -1
            else:
                left = mid + 1
        return result
            


