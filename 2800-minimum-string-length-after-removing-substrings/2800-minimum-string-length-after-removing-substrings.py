class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            if stack:
                tmp = stack[-1] + char
                if tmp == 'AB' or tmp == 'CD':
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return len(stack)