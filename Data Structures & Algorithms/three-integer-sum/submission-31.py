class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                totsum = nums[l]+nums[r]+n
                if totsum > 0:
                    r -= 1
                elif totsum < 0:
                    l += 1
                else:
                    ret.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return ret