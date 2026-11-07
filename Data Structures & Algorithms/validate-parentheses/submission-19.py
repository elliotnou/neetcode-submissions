class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoopen = {"]":"[", ")":"(", "}":"{"}
        for c in s:
            if c in closetoopen.keys():
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
        
