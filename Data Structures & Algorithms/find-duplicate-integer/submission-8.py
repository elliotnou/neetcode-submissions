class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ffloyd's cycle detection algorithm
        # once slow and fast pointers meet, its a random node IN the cycle.
        # to find the start of the cycle, the distance of path from HEAD to start is EQUAL to the distance of slow to start

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        cur = 0
        while cur != slow:
            cur = nums[cur]
            slow = nums[slow]
        
        return slow