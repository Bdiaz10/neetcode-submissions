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
        
        # trueTest = canEat(2)
        # trueTest2 = canEat(3)
        # falseTest = canEat(1)
        # print(trueTest)
        # print(trueTest2)
        # print(falseTest)
        # for i in range(1, max(piles)+1):
        #     if canEat(i):
        #         return i

        res = float("inf")
        left = 1
        right = max(piles) + 1
        while left <= right:
            mid = (left + right) // 2
            if canEat(mid):
                res = min(res, mid)
                right = mid -1
            else:
                left = mid + 1
        
            
        return res