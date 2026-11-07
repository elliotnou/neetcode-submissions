class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n), so no sort 

        numSet = set(nums) # accessing is O(1), duplicates removed.
        maxseq = 0
        count = 0
        for n in numSet:
            if n - 1 not in numSet: # n is a starting value
                count = 1
                curr = n
                while curr+ 1 in numSet: 
                    count += 1
                    curr += 1

            maxseq = max(maxseq, count)
        

        return maxseq

                


