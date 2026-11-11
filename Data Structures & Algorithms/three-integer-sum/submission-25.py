class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force method o(n^3)
        # to reduce to o(n^2), we could iterate through each element of nums as the "anchor"
        # for each anchor, we use a two pointer method to search the remaining RIGHT side of the array for a sum 0
        # edge cases:
            # [-1, -1, -1, 0, 1] -> should only return [[-1, 0, 1]]

        ret = []
        nums.sort()
        
        for i, n in enumerate(nums):
            l, r = i+1, len(nums) - 1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while l < r:
                if n + nums[l] + nums[r] == 0:
                    ret.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    r -= 1
                elif n + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
                    
        
        return ret