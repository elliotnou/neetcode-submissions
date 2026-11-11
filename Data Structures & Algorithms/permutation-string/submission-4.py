class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # only lowercase letters, so use a len 26 array
        # if index i represents the ord(c) - ord('a'), freq[i] represents frequency of that char appearing

        # use a sliding window approach, where the window length must <= len(s1), that is, r-l+1 <= len(s1) at all times

        # keep the WINDOW freq too

        s1freq = [0] * 26
        windowfreq = [0] * 26

        for c in s1:
            s1freq[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            windowfreq[ord(s2[r]) - ord('a')] += 1
            while r-l+1 > len(s1):
                windowfreq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s1freq == windowfreq:
                return True
        
        return False
        
        

