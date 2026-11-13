class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ret = 0
        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r
            ret = max(ret, prices[r]-prices[l])
        
        return ret
            