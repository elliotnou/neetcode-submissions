class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers to iterate on all possible pairs. then, we
        #      check if the negative of their sum exists.
        #       for this, we must check membership

        nums.sort()

        res = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]: # when the chosen k is the same as before, SKIP.
                continue
            
            l, r = k + 1, len(nums)-1 # must start from k + 1 to avoid DUPLICATE scenarios. 

            while l < r:
                if nums[l] + nums[r] == -nums[k]:
                    res.append([nums[l], nums[r], nums[k]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif nums[l] + nums[r] < -nums[k]:
                    l += 1
                elif nums[l] + nums[r] > -nums[k]:
                    r -= 1
        return res
                

