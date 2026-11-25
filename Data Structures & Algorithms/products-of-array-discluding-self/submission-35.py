class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # build a leftarray l where index i is the prdouct of all numbers left of nums[i] in nums. same for right
        # third pass builds ret

        leftarray = [1] * len(nums)
        rightarray = [1] * len(nums)
        ret = []

        for i in range(1, len(nums)):
            leftarray[i] = leftarray[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rightarray[i] = rightarray[i+1] * nums[i+1]

        for i in range(len(nums)):
            ret.append(leftarray[i]*rightarray[i])
        
        return ret

