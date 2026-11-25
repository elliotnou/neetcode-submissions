class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # we know that if nums[m] < nums[r], at least the right half is sorted, so we look on the left for the pivot and INCLUDE m as it may be min

        l, r = 0, len(nums) - 1
        minval = nums[0]
        while l <= r: # we hope to land on min when l==r, so exclude 
            m = (l+r) // 2
            minval = min(minval, nums[m])
            if nums[m] < nums[r]:
                r = m-1
            else:
                l = m+1
        
        return minval