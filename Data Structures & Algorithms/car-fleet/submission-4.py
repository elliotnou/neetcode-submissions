class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we must first sort the list descending - if the position of the car is SMALLER and the time taken is smaller, it merges. if the position of the car is SMALLER adn the time taken is LARGER, it starts (leads) a new fleet.

        # we use a monotonic stack to keep track of the fleets. a faster car will merge into the last car and disappear. a slower car will start a new fleet for the cars behind it.

        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
        