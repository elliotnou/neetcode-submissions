class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        suffix = [1] * len(nums)
        ret = [1] * len(nums)
        for i in range(1, len(nums)):
            ret[i] = ret[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
            ret[i] *= suffix[i]
        return ret

