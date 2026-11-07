class Solution:
    def isValid(self, s: str) -> bool:
        # Input: a string only consisting of (){}[] characters
        # Output: a boolean value that returns true iff string is a valid parentheses
        # Example: "[][{()[]}]" -> true, "]]" -> false
        # Edge cases:
            # "" -> true
            # "]" -> false
            # "[[{" -> false
            # "[]{}()" -> true
        
        # we maintain a stack where we ADD an open parentheses to the top whenever we encounter one, and we PAIR a closed parentheses with the top open parentheses (and remove) when we encounter a lcosed

        # at the end, we want stack to be EMPTY (all open parenthese are paired with a closed parenthese)

        stack = []
        for c in s:
            if (c == "]" or c == "}" or c == ")") and len(stack) == 0:
                return False
            if c == "[" or c == "(" or c == "{":
                stack.append(c)
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
 