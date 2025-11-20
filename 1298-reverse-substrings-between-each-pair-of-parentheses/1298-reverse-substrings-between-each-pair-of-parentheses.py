class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']

        for c in s:
            if c == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop()[::-1])
                stack.pop()
                stack.append(''.join(temp))
            else:
                stack.append(c)

        return ''.join(stack)
            