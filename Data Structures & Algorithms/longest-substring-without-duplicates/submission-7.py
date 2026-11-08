class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # increment r 
        # if the new r is in hashset, move l until not
        # record length

        ret = 0
        l, r = 0, 0
        hs = set()

        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1 
            hs.add(s[r])
            ret = max(ret, r-l+1)
            r += 1
            
            

        return ret