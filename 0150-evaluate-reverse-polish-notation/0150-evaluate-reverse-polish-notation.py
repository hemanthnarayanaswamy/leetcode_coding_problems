class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b): return a + b
        def subtract(a, b): return a - b
        def multiply(a, b): return a * b
        def divide(a, b): return int(a / b)

        stack = []
        signs = {'+': add, '*': multiply, '-': subtract, '/': divide}

        for token in tokens:
            if token not in signs:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                c = signs[token](a,b)
                stack.append(c)
        
        return stack[0]