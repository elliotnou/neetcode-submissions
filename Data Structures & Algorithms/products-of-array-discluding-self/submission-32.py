class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # let us do 2 passes:
        #    first pass: ret[i] is the product of everything to the left of nums[i]
        # second pass: multiply that with everything to the right

        ret = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            ret[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= suffix
            suffix *= nums[i]
        
        return ret