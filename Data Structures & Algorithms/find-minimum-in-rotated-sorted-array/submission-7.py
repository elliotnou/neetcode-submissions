class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # if nums[r] < nums[m] -- pivot is on the right, so minimum is somewhere on the right
        # else, pivot is on the left, so minimum is somewhere on the left, but minimum COULD be nums[m]
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            
            if nums[m] > nums[r]:
                # pivot/min is somewhere on the RIGHT, not including m
                l = m+1
            else:
                # right is in order, so pivot/min is somewhere on the LEFT, including m because m is smaller than r so m could be the min
                r = m

        return nums[r]
