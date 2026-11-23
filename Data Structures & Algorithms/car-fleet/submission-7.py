class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # a car merges into the car in front as one fleet if it reaches it
        # the cars should be sorted based on descending position
        # must calculate the time it takes for each car to reach the target, using t = d/s
        # if the car in a smaller position reaches it in less time than the car in FRONT, it merges into that fleet
        # if not, it's a new fleet. -- stack

        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            t = (target - p) / s
            if not stack or t > stack[-1]:
                stack.append(t)
        

        return len(stack)