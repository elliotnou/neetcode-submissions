class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # character can be anything, so use dict

        # a dictionary cannot be a key (not immutable)
        groups = defaultdict(list)

        for s in strs:
            charfreq = defaultdict(int)
            for c in s:
                charfreq[c] += 1
            groups[frozenset(charfreq.items())].append(s)
        
        return list(groups.values())

