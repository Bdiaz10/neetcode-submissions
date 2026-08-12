class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def canFinish(k: int) -> bool:
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h
        
       
        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            middle = left + ((right - left) // 2)
            if canFinish(middle):
                res = min(res, middle)
                right = middle -1
            else:
                left = middle + 1
        
        return res

