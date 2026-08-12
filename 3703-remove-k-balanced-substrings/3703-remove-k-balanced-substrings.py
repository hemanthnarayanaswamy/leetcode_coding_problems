class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack = []
        res = ''

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if len(stack) >= 2:
                if stack[-2][0] == '(' and min(stack[-1][1], stack[-2][1]) >= k:
                    stack.pop()
                    if stack[-1][1] == k:
                        stack.pop()
                    else:
                        stack[-1][1] -= k
        
        for c, n in stack:
            res += c * n
        
        return res





