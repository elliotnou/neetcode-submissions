class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # traverse nums from left to right
        # keep a leftprod, and set each res[i] to leftprod * res[i-1]

        leftprod = 1
        for i in range(len(nums)):
            res[i] = leftprod
            leftprod *= nums[i]
        
        rightprod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rightprod
            rightprod *= nums[i]
        
        return res




