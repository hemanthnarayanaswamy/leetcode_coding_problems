class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first = second = float('inf')
        for p in prices:
            if p < first:
                second, first = first, p
            elif p < second:
                second = p

        cost = first + second
        return money - cost if cost <= money else money
