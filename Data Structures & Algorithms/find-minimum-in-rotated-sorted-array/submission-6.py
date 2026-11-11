class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # if nums[r] < nums[m] -- pivot is on the right, so minimum is somewhere on the right
        # else, pivot is on the left, so minimum is somewhere on the left, but minimum COULD be nums[m]
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            
            if nums[r] < nums[m]:
                l = m+1
            else:
                r = m

        return nums[l]
