class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn nums into a hashset O(n)
        # for each number in nums, if n - 1 doesn't exist in the set, we know it can be the start of a sequence
        # keep counting until n + 1 doesn't exist
        # return max


        numset = set(nums)
        ret = 0
        for n in numset:
            if n - 1 not in numset:
                count = 1
                while n+count in numset:
                    count += 1
                ret = max(count, ret)
            
        
        return ret 
                

            
                

