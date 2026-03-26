class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        
        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:  # ch == ']'
                if stack:
                    stack.pop()  # balancing closing bracket ] with an open bracket in the stack
        
        # size of stack = number of unbalanced open brackets
        return (len(stack) + 1) // 2
        