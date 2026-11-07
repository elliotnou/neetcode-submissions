class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap where the KEY is an anagram identifier (perhaps a dict of key value pairs that maps character with frequency), and VALUE is a list of strings
        hm = defaultdict(list)
        for s in strs:
            # create a anagram mapping of s
            alist = [0] * 26
            for c in s:
                alist[ord(c) - ord('a')] += 1
            hm[tuple(alist)].append(s) 
        return list(hm.values())