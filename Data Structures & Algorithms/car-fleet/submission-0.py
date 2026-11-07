class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # input: 2 arrays of integers, position and speed, and a destination position target
        # output: number of car fleets at target destination

        # edge cases:
        #   pos = [0, 0, 0, 0], speed = [1, 1, 1, 1] -> 4
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                # new fleet
                stack.append(time)
        
        return(len(stack))
            




