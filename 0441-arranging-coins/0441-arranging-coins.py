class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-0.5 + math.sqrt(2*n + 0.25))