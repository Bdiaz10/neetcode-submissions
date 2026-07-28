class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = [0] * len(prices)
        p = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            maxp[i] = p - prices[i]
            p = max(p, prices[i])
        return max(maxp)

