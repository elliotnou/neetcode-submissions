class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if we find the point in which the number BEFORE is GREATER than the number AFTER, that is the pivot point

        # if left element is GREATER than right element, the pivot is somewhere to the RIGHT
        # if left element is LESS than right element, the pivot is somewhere to the LEFT

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m+1
            if nums[m] < nums[r]:
                r = m
        
        return nums[l]

# if m < r and m > l, Min is on the LEFT (order)
# if m < r and m < l, Min is on the LEFT
# if m > r and m > l, Min is on the RIGHT
# if m > r and m < l, Min is on the RIGHT (order)