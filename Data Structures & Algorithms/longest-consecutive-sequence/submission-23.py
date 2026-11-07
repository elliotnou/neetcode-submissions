# input: array of ints
# output: length of longest number of elements that forms a 1-diff sequence
# edge cases:
#   [] -> 0
#   [1, 3, 5] -> 1
#   [3] -> 1
#   [-1, 0, 1] -> 3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ret = 0
        for n in numset:
            length = 1
            if n-1 not in numset: # start of a sequence
                while n+length in numset:
                    length += 1
                ret = max(ret, length)
        
        return ret

