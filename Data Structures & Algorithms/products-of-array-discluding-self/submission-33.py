class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # keep track of the prefix product
        # multiply the suffix product to it

        prefix = 1
        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= suffix
            suffix *= nums[i]
        
        return ret

