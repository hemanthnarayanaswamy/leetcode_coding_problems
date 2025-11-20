class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ')':
                print(f'we have found the ( {stack}')
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop()[::-1])
                print(f'This is temp {temp}')
                stack.pop()
                stack.append(''.join(temp))
            else:
                stack.append(c)
                print(stack)

        return ''.join(stack) if stack else ''
            