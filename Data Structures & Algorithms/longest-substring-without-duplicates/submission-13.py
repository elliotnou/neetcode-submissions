class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # maintain a list (all lowercase alphabet)

        freq = set()

        l = 0
        ret = 0
        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l += 1

            freq.add(s[r])
            ret = max(ret, r - l + 1)
        
        return ret



