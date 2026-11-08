class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we want to check for membership whether the n-1 is in teh array, so we use a set
        numset = set(nums)

        # we only try making a consecutive seq if n-1 is NOT in the set, as it is a beginning
        ret = 0
        for n in numset:
            if n - 1 not in numset:
                length = 1
                while n+length in numset:
                    length += 1
                ret = max(ret, length)
        
        return ret