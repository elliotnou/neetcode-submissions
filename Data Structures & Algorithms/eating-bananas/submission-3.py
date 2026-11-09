class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the possible speed is bound by [1, max(piles)]
        # we do a binary search on the possible speeds
            # at each search, we compute whether it can finish in h time
            # if it can finish, SAVE that min and search left (finding minimum)
            # if it can't finish, search right
            
        l, r = 1, max(piles)
        minspeed = max(piles)
        while l <= r:
            m = (l + r) // 2
            t = 0
            for p in piles:
                t += -(-p//m)
            if t > h:
                # takes too much time, search right
                l = m + 1
            elif t <= h:
                minspeed = m
                r = m - 1
        return minspeed


