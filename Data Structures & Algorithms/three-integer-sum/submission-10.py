class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers to iterate on all possible pairs. then, we
        #      check if the negative of their sum exists.
        #       for this, we must check membership

        # [-4, -1, -1, 0, 1, 2]
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i == 0 or nums[i] != nums[i-1]:
                l,r = i+1, len(nums) - 1
                while l < len(nums) and l < r:
                    tot = nums[i] + nums[l] + nums[r]
                    if tot > 0:
                        r -= 1
                    elif tot < 0:
                        l += 1
                        while l < len(nums) and nums[l-1] == nums[l]:
                            l += 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while l < len(nums) and nums[l-1] == nums[l]:
                            l += 1
                        r -= 1

            
        return res


