class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # keep a hashset of chars in window
        # move right. when adjust window so that window doesnt include any chars in the hashset
        # then, compute max

        ret = 0
        l = 0
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            ret = max(ret, r-l+1)
        
        return ret
            
