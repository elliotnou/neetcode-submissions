class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # maintain a stack. push if its a number
        # if its an operator, pop the two two, evaluate, and push

        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
                continue
            
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            
        return stack[0]
