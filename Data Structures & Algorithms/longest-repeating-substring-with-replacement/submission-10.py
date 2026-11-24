class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we maintain a list of length 26
        # the length of the window - the maximum value of the list must be LESS THAN OR EQUAL TO K at all times

        l = 0
        freq = [0] * 26
        ret = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            if (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            ret = max(ret, r - l + 1)
        
        return ret
            
            
