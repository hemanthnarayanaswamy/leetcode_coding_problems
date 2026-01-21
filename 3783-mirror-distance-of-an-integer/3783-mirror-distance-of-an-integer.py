class Solution:
    def mirrorDistance(self, n: int) -> int:
        def mirrorNum(n):
            res = 0
            while n:
                res = res*10 + (n % 10)
                n //= 10
            return res
        
        mn = mirrorNum(n)
        return abs(n - mn)
