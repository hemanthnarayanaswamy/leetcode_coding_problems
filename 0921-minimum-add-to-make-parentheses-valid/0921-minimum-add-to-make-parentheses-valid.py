class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        toAdd = 0

        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                toAdd += 1
        
        toAdd += len(stack)

        return toAdd
            