class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)


        while l < r:
            m = (l + r) // 2
            t = 0
            for p in piles:
                t += math.ceil(float(p) / m)
            
            if t <= h:
                # search left for more minimum, but minimum could be l
                r = m
            else:
                l = m+1
        
        return l

