class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        nums.sort()

        for i, n in enumerate(nums):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                totsum = n + nums[l] + nums[r]
                if totsum < 0:
                    l += 1
                elif totsum > 0:
                    r -= 1
                else:
                    ret.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return ret
