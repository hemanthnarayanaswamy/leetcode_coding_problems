class Solution:
    def maxDistinct(self, s: str) -> int:
        distinctChar = set()

        for c in s:
            if c not in distinctChar:
                distinctChar.add(c)
        
        return len(distinctChar)