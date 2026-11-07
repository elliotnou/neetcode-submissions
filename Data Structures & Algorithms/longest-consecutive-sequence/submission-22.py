class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ret = 0
        for n in numset:
            if n-1 not in numset:
                maxseq = 1
                while n+maxseq in numset:
                    maxseq += 1
                ret = max(ret, maxseq)
        
        return ret
