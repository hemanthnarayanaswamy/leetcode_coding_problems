class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        s = 0
        p = 1

        while num:
            q, r = divmod(num, 10)
            s += r
            p *= r
            num = q

        return n % (s+p) == 0
