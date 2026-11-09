class Solution:
    def isValid(self, s: str) -> bool:
        # open brackets are added to the stack
        # closed bracket, see if its openpair is the ToS. if yes, pop. if no, return False

        closetoopen = {"]":"[", "}":"{", ")":"("}

        stack = []
        for c in s:
            if c in closetoopen.keys():
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        
        if stack:
            return False
        else:
            return True