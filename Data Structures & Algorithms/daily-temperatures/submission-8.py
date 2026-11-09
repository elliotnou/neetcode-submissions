class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # when there is a temperature that is greater, we calculate the distance in index from that temp to whatever's smaller than it
        # monotonic stack.
        
        ret = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ret[j] = i-j
            stack.append(i)
        
        return ret