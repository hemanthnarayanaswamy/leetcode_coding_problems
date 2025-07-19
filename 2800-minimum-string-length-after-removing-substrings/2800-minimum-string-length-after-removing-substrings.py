class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        removeCond = ('AB', 'CD')

        for char in s:
            if stack:
                if stack[-1] + char in removeCond:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return len(stack)