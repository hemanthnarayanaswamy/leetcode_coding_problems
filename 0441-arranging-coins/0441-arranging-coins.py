class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        rows = 0

        while i <= n:
            n -= i
            rows += 1
            i += 1
        
        return rows