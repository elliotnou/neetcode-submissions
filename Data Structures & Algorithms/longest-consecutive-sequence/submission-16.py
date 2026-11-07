class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n), so no sort 

        # first, we wanna access elements continuously quickly
        # further, we dont care about the ORDER of nums nor the duplicates.
        numSet = set(nums)

        maxcount = 0
        for n in numSet:
            count = 1
            if n - 1 not in numSet: # start of a sequence
                # check longest sequence
                m = n
                count = 1
                while m + 1 in numSet:
                    count += 1
                    m += 1
                maxcount = max(count, maxcount)
        return maxcount






        
                


