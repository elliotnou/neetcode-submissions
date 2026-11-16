class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window,
        
        substring = set()
        ret = 0

        l = 0
        for r in range(len(s)):
            
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            ret = max(ret, r - l + 1)
            substring.add(s[r])

        
        return ret
            