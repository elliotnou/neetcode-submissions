class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # when a bigger temp is reached, keep popping and store the difference 

        stack = [] # store indices
        ret = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:  
                j = stack.pop()
                ret[j] = i - j
            stack.append(i)
        
        return ret
        

