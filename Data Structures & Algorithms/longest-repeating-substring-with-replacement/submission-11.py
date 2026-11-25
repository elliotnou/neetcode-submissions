class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # the window shud be adjusted so that the windowsize r-l+1 MINUS the greatest occurrence should be LESS THAN OR EQUAL TO k at all times, that is, adjus the window if that is > k

        windowfreq = [0] * 26
        l = 0
        ret = 0
        for r in range(len(s)):
            windowfreq[ord(s[r]) - ord('A')] += 1
            while (r-l+1) - max(windowfreq) > k:
                windowfreq[ord(s[l]) - ord('A')] -= 1
                l += 1
            ret = max(ret, r-l+1)
        
        return ret

        
        
