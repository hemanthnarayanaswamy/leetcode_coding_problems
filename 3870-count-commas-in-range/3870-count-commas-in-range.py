class Solution:
    def countCommas(self, n: int) -> int:
        res = n - 999
        return res if res > 0 else 0