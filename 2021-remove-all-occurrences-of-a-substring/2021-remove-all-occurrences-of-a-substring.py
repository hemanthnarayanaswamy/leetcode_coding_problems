class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        p = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= p and ''.join(stack[-p:]) == part:
                for _ in range(p):
                    stack.pop()
        
        return ''.join(stack)
