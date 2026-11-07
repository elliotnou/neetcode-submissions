class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums) - 1
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if n + nums[l] + nums[r] < 0:
                    l += 1
                elif n + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r: l += 1
                        
        return res
                    