class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recur(s, open, closed):
            if open == closed == n:
                res.append(s)
                return
            
            if open < n:
                recur(s + "(", open+1, closed)
            if closed < open:
                recur(s + ")", open, closed+1)
            
        recur("", 0, 0)
        return res

        

