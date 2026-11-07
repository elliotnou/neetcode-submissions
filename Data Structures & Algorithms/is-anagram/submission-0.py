class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary where key is CHAR and value is INT 
        hms = defaultdict(int)
        hmt = defaultdict(int)
        if len(s) != len(t):
            return False
        for i, c in enumerate(s):
            hms[s[i]] = hms.get(s[i], 0) + 1
            hmt[t[i]] = hmt.get(t[i], 0) + 1
        
        if hms == hmt:
            return True
        else:
            return False
