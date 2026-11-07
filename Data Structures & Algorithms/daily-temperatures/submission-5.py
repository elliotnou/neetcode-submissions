class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        # let stack be [temp, index]
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            # if the element is bigger than the prev
            while stack and t > temperatures[stack[-1]]:
                stackInd = stack.pop()
                stackT = temperatures[stackInd]
                res[stackInd] = i - stackInd
            stack.append(i)
        return res






            
