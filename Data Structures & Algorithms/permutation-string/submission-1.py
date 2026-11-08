class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # first instinct - dict and membership check... but the chars must be together, not just IN it.
        # perhaps sliding window until the window's dict matches the input

        s1count = [0] * 26
        windowcount = [0] * 26

        for c in s1:
            s1count[ord(c) - ord('a')] += 1
        
        l,r = 0,0

        for r in range(len(s2)):
            
        
            
            
            windowcount[ord(s2[r]) - ord('a')] += 1
            if r-l+1 > len(s1):
                windowcount[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if s1count == windowcount:
                return True
             

        return False
        