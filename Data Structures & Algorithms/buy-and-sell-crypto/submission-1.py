class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sells = [0] * len(prices) # sells[i] = rightMax - prices[i]
        maxP = 0
        rightMax = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            #sells[i] = rightMax - prices[i]
            maxP = max(rightMax - prices[i], maxP)
            rightMax = max(rightMax, prices[i])
            
        return maxP


