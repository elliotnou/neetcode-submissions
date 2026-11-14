class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # some type of stack
        # assumign its monotonic because everytime a greater value appears, it should probably pop all the lesser and ADD the difference.
        # leads me to believe stack should store indices

        stack = []
        ret = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ret[j] = i-j
            
            stack.append(i)
        
        return ret