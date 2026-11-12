class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # when will a fleet be created? when a car that is at a FURTHER position reaches the target in LESS time than a car in a LESSER position. 
        cars = sorted(zip(position, speed), reverse=True)
        fleets = []
        for p, s in cars:
            t = (target - p) / s
            if not fleets or fleets[-1] < t:
                fleets.append(t)
        
        return len(fleets)
