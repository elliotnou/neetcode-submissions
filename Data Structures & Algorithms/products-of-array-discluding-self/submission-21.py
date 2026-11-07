class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: array of ints, duplicates allowed
        # Output: array of ints where each element is the product of all elements except        itself
        # Example: [1, 5, 3, 6, -1] -> [-90, -18, -30, -15, 90]
        # Edge cases:
            # [1, 2] -> [2, 1]
            # [0, 1, 2, 3] -> [6, 0, 0, 0]
            # [1, 1, 1] -> [1, 1, 1]
            # [-1 -1 -1 -1] -> [-1, -1, -1, -1]
        # Brute force: for every element index i in output, iterate through the whole of nums and multiply every number that isn't nums[i] O(n^2)
        # To fix this so we dont have to recreate the product we ALREADY created in the previous run, we can maintain a left product and right product.

        leftprod = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            leftprod[i] = leftprod[i-1] * nums[i-1]
        
        rightprod = [1 for i in range(len(nums))]
        for i in range(len(nums)-2, -1, -1):
            rightprod[i] = rightprod[i+1] * nums[i+1]
        
        ret = []
        for i in range(len(nums)):
            ret.append(leftprod[i]*rightprod[i])
        return ret

        
