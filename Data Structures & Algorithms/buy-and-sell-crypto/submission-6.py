class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we use a sliding window approach
        # when the right side is LESS than the left pointer, always jump to RIGHT.
        # log the max profit along the way

        ret = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            ret = max(ret, prices[r] - prices[l])
        
        return ret
        
