class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        f = s = float("inf")

        for pos in range(len(prices)):
            if prices[pos] <= f:
                s = f
                f = prices[pos]
            elif prices[pos] < s:
                s = prices[pos]

        if money >= f + s:
            return money - f - s
        return money