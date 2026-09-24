class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = prices[-1]
        res = 0
        for i in range(len(prices)-2, -1, -1):
            profit = currMax - prices[i]
            currMax = max(prices[i], currMax)
            res = max(profit, res)
        return res