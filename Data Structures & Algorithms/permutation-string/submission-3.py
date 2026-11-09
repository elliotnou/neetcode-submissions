class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # since we are checking for permutation (chars must be together), the window must be at most length of s1

        # adjustment critera: window <= len(s1)

        # at each window, we are checking if the char:frequency array is equal

        s1freq = [0] * 26
        windowfreq = [0] * 26

        for c in s1:
            s1freq[ord(c) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            while r-l+1 > len(s1):
                windowfreq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            windowfreq[ord(s2[r]) - ord('a')] += 1
            if s1freq == windowfreq:
                return True
        return False