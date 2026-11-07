class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        # go through, if smaller then the top of stack, push
            # if larger than top of stack, keep popping until its not larger, and store the difference in index at the index of the popped.
        res = [0] * len(temperatures)
        stack = [] # stack of INDICES
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)

        return res


            
