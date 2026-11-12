class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow, fast which goes to the index supposed by nums[i]

        # once slow == fast (guaranteed), then 

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        
        # cycle is found.
        walk = 0
        while True:
            walk = nums[walk]
            slow = nums[slow]
            if walk == slow:
                return slow
        