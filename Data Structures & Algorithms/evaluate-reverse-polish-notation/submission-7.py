class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"

        stack = []

        for c in tokens:
            if c not in operators:
                stack.append(int(c))
                continue
            else:
                if c == "+":
                    stack.append(stack.pop() + stack.pop())
                elif c == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                elif c == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))

        return stack[0]