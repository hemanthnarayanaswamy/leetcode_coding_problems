class Solution:
    def resultingString(self, s: str) -> str:
        stack = [] 

        for c in s:
            if stack:
                val = abs(ord(stack[-1]) - ord(c))
                if val == 1 or val == 25:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
            
        return ''.join(stack)
