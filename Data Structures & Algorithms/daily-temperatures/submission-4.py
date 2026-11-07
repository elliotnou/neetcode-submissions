class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        # let stack be [temp, index]
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            # if the element is bigger than the prev
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t, i])
        return res






            
