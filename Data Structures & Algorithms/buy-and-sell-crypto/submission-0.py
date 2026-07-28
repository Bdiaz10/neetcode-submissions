class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sells = [0] * len(prices) # sells[i] = rightMax - prices[i]
        rightMax = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            sells[i] = rightMax - prices[i]
            rightMax = max(rightMax, prices[i])
            
        print(sells)
        return max(sells)


