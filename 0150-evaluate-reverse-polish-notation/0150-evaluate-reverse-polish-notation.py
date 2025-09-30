class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b): return a + b
        def subtract(a, b): return a - b
        def multiply(a, b): return a * b
        def divide(a, b): return int(a / b)

        stack = []
        signs = {'+': add, '*': multiply, '-': subtract, '/': divide}
        
        for token in tokens:
            if token in signs:
                b = stack.pop()
                a = stack.pop()
                c = signs[token](a,b)
                stack.append(c)
            else:
                stack.append(int(token))

        return stack[0]