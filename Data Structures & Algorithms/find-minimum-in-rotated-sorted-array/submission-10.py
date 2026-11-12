class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if middle > right, the pivot is on the right somewhere
        # else, the pivot is on the left somewhere and COULD be middle
        
        l, r = 0, len(nums) - 1
        ret = nums[0]
        while l <= r: # since when l == r we want that to be the min
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m+1
            else:
                ret = min(ret, nums[m])
                r = m-1
        
        return ret