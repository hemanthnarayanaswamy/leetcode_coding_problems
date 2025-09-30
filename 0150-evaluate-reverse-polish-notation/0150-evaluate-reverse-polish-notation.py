class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                result = ops[token](a, b)
                stack.append(int(result))  
            else:
                stack.append(int(token))
        
        return stack[0]