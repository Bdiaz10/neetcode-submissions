class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = prices[-1]
        res = 0
        for n in reversed(prices[:len(prices)-1]):
            res = max(res, currMax - n)
            currMax = max(currMax, n)
        return res