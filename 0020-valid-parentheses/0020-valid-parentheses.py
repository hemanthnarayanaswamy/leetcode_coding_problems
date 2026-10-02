class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "{" : "}", "[" : "]"}
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack and char == brackets[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return not stack   