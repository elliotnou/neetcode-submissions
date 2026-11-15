class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # an aangram is unique from its frequency of characters. 
        # strs[i] is made up of lowercase, so we use a 26 length array

        groups = defaultdict(list)

        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            groups[tuple(freq)].append(s)
        
        return list(groups.values())

