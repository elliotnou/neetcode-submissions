class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a dict with character and its occurrencds
        # at each r, we adjust the window until (r-l+1) - max(dict.values()) <= k

        chars = [0] * 26

        l = 0
        ret = 0
        for r in range(len(s)):
            chars[ord(s[r]) - ord('A')] += 1
            while (r-l+1) - max(chars) > k:
                chars[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            
            
            ret = max(ret, r-l+1)
        
        return ret
