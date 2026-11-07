class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap where the KEY is an anagram identifier (perhaps a dict of key value pairs that maps character with frequency), and VALUE is a list of strings
        hm = defaultdict(list)
        for s in strs:
            # create a anagram mapping of s
            amap = {i: 0 for i in range(97, 123)}
            for c in s:
                amap[ord(c)] += 1
            hm[tuple(amap.values())].append(s) 
        return list(hm.values())