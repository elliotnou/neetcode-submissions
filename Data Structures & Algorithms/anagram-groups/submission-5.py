class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap of each string where keys are 'a' to 'z' and values are the number of occurrences

        res = defaultdict(list)
        for s in strs:
            hashmap = [0]*26
            for c in s:
                hashmap[ord(c)-ord('a')] += 1
            res[tuple(hashmap)].append(s)
        
        return list(res.values())
            
