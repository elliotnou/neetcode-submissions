class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep moving r 
        # at any time if prices[r] > prices[l], move l to r
        # record the max at all

        l,r = 0,0
        maxret = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            maxret = max(maxret, prices[r]-prices[l])
            r += 1
        return maxret
            
            