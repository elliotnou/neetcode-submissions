class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # there is a finite number of speeds we can try -- 1 to max(piles)
        # we use a binary search for the smallest value that completes 


        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            t = 0
            for p in piles:
                t += -(-p // m)
            if t <= h:
                r = m
            else:
                l = m + 1
        
        return l
