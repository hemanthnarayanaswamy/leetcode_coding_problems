class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        openCount = closeCount = 0
        res = ''
        idx = 0

        for i in range(len(s)):
            if s[i] == '(':
                openCount += 1
            else:
                closeCount += 1

            if openCount == closeCount:
                res += s[idx+1:i]
                idx = i+1

        return res

            
