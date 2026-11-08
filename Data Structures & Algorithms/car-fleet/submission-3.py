class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we must first sort the cars by POSITION, greatest to least
        # then, calculate the time it takes for each car to reach target
        # if a car in a further position takes LESS time as the car in front, this merges into the fleet with that car. 
        # if a car in a further position takes MORE time as the car in front, this creates a NEW fleet for the cars BEHIND it, so it shud be added to the stack.

        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            t = (target - p) / s
            # no new fleet
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
