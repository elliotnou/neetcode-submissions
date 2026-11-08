class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input: string with only uppercase characters, int k
        # output: longest substring of s, after k replacements of characters in s, with the same characters


        # AAABABB, k = 1. we find the longest substring with k foreign characters
        # using sliding window,
        # maintain a hashset where MAX length can be 1+k. If the window comes across a character that is in hs, don't add. if it ISNT in hs, add. if length gets greater than 1+k, adjust window until it isn't. 
        # record max length at each


        # main is the char with MORE occurrences (A)
        # rest is the sum of occurrences of all other chars, <= k
        maxlen = 0
        hm = defaultdict(int)

        # mainchar C is the char with most occurrences F
        # the rest are summed, must be <= k

        # if another char has more occurrences then F, mainchar C becomes that char and F becomes that.
        l, r = 0, 0
        while r < len(s):
            hm[s[r]] += 1
            while (r-l+1) - max(hm.values()) > k:
                # decrement hm(s[l])
                hm[s[l]] -= 1
                # if hm(s[l]) == 0, hs.remove(s[l])
                l += 1
            maxlen = max(maxlen, r-l+1)
            
            r += 1
            
            
        return maxlen

