class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers to iterate on all possible pairs. then, we
        #      check if the negative of their sum exists.
        #       for this, we must check membership

        nums.sort()

        res = []
        for k in range(len(nums)):

            
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            
            l, r = k + 1, len(nums)-1
            while l < r:
                if l == k:
                    l += 1
                if r == k:
                    r -= 1
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
                

