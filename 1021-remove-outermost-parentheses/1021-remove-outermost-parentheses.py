class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        dep = 0

        for ch in s:
            if ch == '(':
                if dep > 0:
                    res.append(ch)
                dep += 1
            else:
                dep -= 1
                if dep > 0:
                    res.append(ch)

        return ''.join(res)