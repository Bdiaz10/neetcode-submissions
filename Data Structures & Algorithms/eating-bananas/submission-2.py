import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(n: int) -> bool:
            currentHours = 0
            for b in piles:
                val = (b / n)
                currentHours += math.ceil(val)
                if currentHours > h:
                    return False
            return True
        
        res = 0
        left = 1
        right = max(piles) + 1
        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                res = mid
                right = mid -1
            else:
                left = mid + 1
        
            
        return res