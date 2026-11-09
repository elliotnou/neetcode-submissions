class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # three things to track -- open brackets, closed brackets
        # if open brackets < n, we can open a bracket
        # further, not or, if open brackets < closed brackets, we can close a bracket

        ret = []
        def backTrack(s, open, close):
            if n == open == close:
                ret.append("".join(s))
                return
            
            if open < n:
                s.append("(")
                backTrack(s, open+1, close)
                s.pop()
            if open > close:
                s.append(")")
                backTrack(s, open, close+1)
                s.pop()
        
        backTrack([], 0, 0)
        return ret