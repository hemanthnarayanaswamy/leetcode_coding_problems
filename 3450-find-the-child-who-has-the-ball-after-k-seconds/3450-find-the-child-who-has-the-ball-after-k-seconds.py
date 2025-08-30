class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        n -= 1
        m = k % n
        q = k // n

        if q % 2:
            return n - m 
        else:
            return m