class Solution:
    def isValid(self, s: str) -> bool:
        # iterate through the string s
        # if its one of the open brackets, add to stack
        # if its one of the closed brackets, check if it corresponds to an open of the        same sort on the top of the stack (i.e. end of the array)

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[': # open bracket
                stack += c
            else: # closed bracket
                if len(stack) == 0:
                    return False
                if (c == ')' and stack[-1] == '(') or (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{'):
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
                

