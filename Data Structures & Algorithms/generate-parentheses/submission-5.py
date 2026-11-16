class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []

        def dfs(open, closed):
            if open == closed == n:
                ret.append("".join(stack))
                return
            if open > closed:
                stack.append(")")
                dfs(open, closed+1)
                stack.pop()
            if open < n:
                stack.append("(")
                dfs(open+1, closed)
                stack.pop()
        
            
        dfs(0, 0)
        return ret