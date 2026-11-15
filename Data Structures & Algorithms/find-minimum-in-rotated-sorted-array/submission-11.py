class Solution:
    def findMin(self, nums: List[int]) -> int:
        # we use a binary serach appraoch
        # if the middle value is LESS then the right value, the RIGHT half must be sorted ascending (i.e. pivot is somewhere on the LEFT, but include the current m as it MAY be the min)
        # if not, the pivot is somewhere on the RIGHT (no need to include the current middle because its NOT the min)
        # when l == r, it should land on the min, so loop is l < r not l <= r

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]