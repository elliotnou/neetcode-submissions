class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        best = 0
        ht = set()
        # keep move r forward, add s[r] to hashset. if s[r] is a duplicate, keep moving s[l] forward until l == r or until s[r] no longer in hashset
        # is s[l] is in the hashset, move l forward until it ISNT
        for r in range(len(s)):
            while s[r] in ht:
                ht.remove(s[l])
                l += 1
            
            ht.add(s[r])
            
            best = max(best, r-l+1) 
            

            # if l is r - 1, MUST r += 1
            # if s[r] is not s[l], r += 1
            # if s[r] is s[l], l += 1
        return best