class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        openCount = closeCount = 0
        res = ''
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == '(':
                openCount += 1
            else:
                closeCount += 1

            if openCount == closeCount:
                stack.pop()
                stack.pop(0)
                res += ''.join(stack)
                stack = []

        return res

            
