class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the eating speed can be anywhere between [1, max(piles)]

        # one pile takes -(-pile // k) time 

        l, r = 1, max(piles)

        res = r
        while l <= r:
            hours = 0
            k = (l + r) // 2
            for p in piles:
                hours += -(-p // k)
            
            if hours <= h:
                res = k
                # search smaller
                r = k -1
            else:
                l = k + 1
        return res



