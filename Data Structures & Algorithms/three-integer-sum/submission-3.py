class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers to iterate on all possible pairs. then, we
        #      check if the negative of their sum exists.
        #       for this, we must check membership

        nums.sort()

        # iterate through the array, designating each element as the k.
        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k-1]: # case where k is the same as before (causing duplicates)
                continue
            
            l, r = k + 1, len(nums)-1
            while l < r:
                threesum = nums[l] + nums[r] + nums[k]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else: # when threesum = 0
                    res.append([nums[l], nums[r], nums[k]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res





