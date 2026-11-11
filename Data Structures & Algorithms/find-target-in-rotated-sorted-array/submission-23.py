class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search
        # if nums[l] < nums[m], then we know the left side is ascending in order.
            # if target is between nums[l] and nums[m], then search left
            # else, search right
        
        # if nums[m] < nums[r] then we know the right side is ascending in order.
            # if trget is between nums[m] and nums[r], then search right.
            # else, search left
    
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        
        return -1