class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens:
            if v in ("+", "-", "*", "/"):
                b = int(stack.pop())
                a = int(stack.pop())
                if v == "+":
                    stack.append(a + b)
                if v == "-":
                    stack.append(a - b)
                if v == "*":
                    stack.append(a * b)
                if v == "/":
                    stack.append(a / b)
            else:
                stack.append(v)
        return int(stack[0])
