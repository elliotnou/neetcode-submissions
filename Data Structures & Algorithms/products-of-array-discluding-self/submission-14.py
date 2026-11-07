class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # we keep a left array where each element is the multiplication of everything to the left of that index
        # we keep a right array

        left = [1] * n
        right = [1] * n
    

        for i in range(n):
            if i > 0:
                left[i] = nums[i-1] * left[i-1]
            else:
                left[i] = 1
        
        for j in range(n-1, -1, -1):
            if j < n-1:
                right[j] = nums[j+1] * right[j+1]
            else:
                right[j] = 1

        res = []
        for m in range(len(nums)):
            res.append(left[m] * right[m])
        return res


