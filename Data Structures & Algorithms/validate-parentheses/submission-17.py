class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedtoopen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c not in ")]}":
                stack.append(c)
            elif len(stack) >= 1 and closedtoopen[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False


        