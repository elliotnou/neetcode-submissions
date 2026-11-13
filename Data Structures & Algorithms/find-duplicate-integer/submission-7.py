class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # ffloyd's cycle detection. 
        # start a slow and a fast pointer, treating the array as a linked list
        # the point at which the slow and fast pointer meets is the same dist as the beginning to the start of the cycle (which is the duplicate number)

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
        


        
