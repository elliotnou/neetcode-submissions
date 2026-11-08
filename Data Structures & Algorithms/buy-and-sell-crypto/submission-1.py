class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        # only move r forward if its bigger, or l is behind it
        # if r+1 is smaller, move l forward

        l = 0
        r = l+1

        while r < len(prices):
            ret = max(ret, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        return ret
                
            
        

