class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if m is > l, then l is the sorted section. check for target there
        # if m < r, then r is the sorted. check for target there.

        l,r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                r = m-1

        return -1
        

