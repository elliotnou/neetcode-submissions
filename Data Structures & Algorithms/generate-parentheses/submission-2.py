class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        s = []
        res = []
        def backTrack(open, closed):
            # if n == open == closed, we want to retrn
            # if open < n, backtrack with a new "("
            # and if open > closed, backtrack with a new ")"

            if n == open == closed:
                res.append("".join(s))
                return
            
            if open < n:
                s.append("(")
                backTrack(open+1, closed)
                s.pop()
            if closed < open:
                s.append(")")
                backTrack(open, closed+1)
                s.pop()
            
        
        backTrack(0, 0)
        return res