class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        n -= 1
        m = time % n
        q = time // n

        if q % 2:
            return n - m + 1
        return m + 1