class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initialize hash array
        # iterate over the elements; check membership in the hash array. if it exists, return false. if not, add to the hash and keep going.
        hs = set()
        for i, n in enumerate(nums):
            if n in hs:
                return True
            else:
                hs.add(n)
        return False
        
        