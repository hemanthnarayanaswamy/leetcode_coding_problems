class Solution:
    def maxDistinct(self, s: str) -> int:
        distinct = set()
        count = 0

        for c in s:
            if c not in distinct:
                count += 1
                distinct.add(c)
        
        return count
