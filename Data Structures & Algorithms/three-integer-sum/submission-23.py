class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # for each anchor, we use a two pointer approach to find summing up to 0

        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums) - 1
            while l < r:
                if n + nums[l] + nums[r] < 0:
                    l += 1
                elif n + nums[l] + nums[r] > 0:
                    r -= 1
                else: # equals 0
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
