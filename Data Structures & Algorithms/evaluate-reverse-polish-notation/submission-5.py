class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # loop through all tokens moving it into a stack
        # is operand, take top two elements, perform the operation, replace.
        operators = {"+", "*", "/", "-"}

        10 * (6 / ((9 + 3) * -11 )) + 17 + 5
        stack = []
        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(a/b))
                elif t == "-":
                    stack.append(a - b)
            else:
                stack.append(int(t))
        
        return stack[0]

