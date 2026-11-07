class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n), so no sort 

        # first, we wanna access elements continuously quickly
        numSet = set(nums)

        maxseq = 0

        for n in nums:
            if n - 1 not in numSet: # good, this is a starting point
                length = 1
                while n + length in numSet:
                    length += 1
            
                maxseq = max(length, maxseq)
        
        return maxseq
                


