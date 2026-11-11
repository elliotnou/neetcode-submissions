class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we maintain a sliding window
        # we also maintain an array freq where index is ord(c) - ord('A') and freq[i] is the number of times it appears in the window
        # at any moment, if max(freq) - (r-l+1) > k, adjust window so that its not

        freq = [0]*26
        l = 0
        ret = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            while (r-l+1) - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            ret = max(ret, r-l+1)
        
        return ret
            
