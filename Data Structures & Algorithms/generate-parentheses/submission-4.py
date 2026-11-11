class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        ret = []

        def backTrack(open, close):
            if open == n == close:
                ret.append("".join(stack))
                return
                
            if open < n:
                stack.append("(")
                backTrack(open+1, close)
                stack.pop()
            if open > close:
                stack.append(")")
                backTrack(open, close+1)
                stack.pop()
        
        backTrack(0, 0)
        return ret
