class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0

        maxprofit = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                maxprofit = max(maxprofit, prices[r] - prices[l])
        
        return maxprofit


