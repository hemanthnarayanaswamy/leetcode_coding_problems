class Solution:
    def mirrorDistance(self, n: int) -> int:
        def mirrorNum(n):
            res = 0
            while n:
                quotient, remainder = divmod(n, 10)
                res = res*10 + remainder
                n = quotient
            return res
        
        mn = mirrorNum(n)
        return abs(n - mn)
