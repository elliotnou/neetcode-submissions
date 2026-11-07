class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = defaultdict(list)
        for s in strs:
            charlist = [0]*26
            for c in s:
                charlist[ord(c) - ord('a')] += 1
            strdict[tuple(charlist)].append(s)
        
        return list(strdict.values())
