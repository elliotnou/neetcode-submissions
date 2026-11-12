class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a set of characters in the window
        # for every r, we adjust the window so that s[r] is NOT in the window

        visited = set()
        l = 0
        ret = 0
        for r in range(len(s)):
        
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            ret = max(ret, r - l + 1)
            visited.add(s[r])
        
        return ret
        

