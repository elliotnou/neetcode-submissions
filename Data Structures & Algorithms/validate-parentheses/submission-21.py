class Solution:
    def isValid(self, s: str) -> bool:
        # for cleaner code, we perhaps want something that quickly finds the open bracket matching of a closed bracket.

        closetoopen = {"]":"[", ")":"(", "}":"{"}

        stack = []
        for c in s:
            if c not in closetoopen:
                stack.append(c)
            elif stack and stack[-1] == closetoopen[c]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False