class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # keep an array
        s1freq = [0] * 26
        for c in s1:
            s1freq[ord(c) - ord('a')] += 1
        
        windowfreq = [0] * 26
        l = 0
        for r in range(len(s2)):
            windowfreq[ord(s2[r]) - ord('a')] += 1
            if r-l+1 > len(s1):
                windowfreq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s1freq == windowfreq:
                return True
    
        return False
            