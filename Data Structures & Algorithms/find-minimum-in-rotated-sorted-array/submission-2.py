class Solution:
    def findMin(self, nums: List[int]) -> int:
         # if m > r then min on the right
         # if m < l then min on the left

        l, r = 0, len(nums) -1
        # if m is on the right, and r is on the left. we do a 
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
            
        return nums[l]

        # if m > r and m > l and l > r then on the RIGHT
        # if m < r and m > l and l > r then on the LEFT
        # if m > r and m > l and l < r Not possible?
        # if m < r and m > l and l < r then

        