class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car only merges into a fleet if its in a SMALLER position (relative to the target) and it takes less time to reach the target than the car right in front of it

        # stack data structure -- if a car merges into front, it is popped
        
        cars = sorted(zip(position, speed), reverse=True) # O(nlogn)
        stack = []

        for p, s in cars:
            # we compute the time taken to reach target
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t) # new fleet
            
            
        return len(stack)

