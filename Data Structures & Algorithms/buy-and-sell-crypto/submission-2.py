class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        for i in range(len(prices)):
            maxp = max(maxp, max(prices[i:]) - prices[i])
        return maxp