class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        p = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxp = max(maxp, p - prices[i])
            p = max(p, prices[i])
        return maxp

