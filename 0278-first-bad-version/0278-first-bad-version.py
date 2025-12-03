# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        h = n 

        while l < h:
            m = (l + h)//2 
            if isBadVersion(m):
                h = m
            else: 
                l = m + 1
        
        return l
