class Solution:
    def maxDepth(self, s: str) -> int:
        depth = maxDepth = 0

        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                maxDepth = max(maxDepth, depth)
                depth -= 1
                
        return maxDepth