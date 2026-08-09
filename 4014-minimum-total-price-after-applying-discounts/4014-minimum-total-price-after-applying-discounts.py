class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        discounts.sort(reverse=True)
        prices.sort(reverse=True)

        for i in range(min(len(discounts), len(prices))):
            p = prices[i]
            prices[i] = p * (100 - discounts[i]) / 100
        
        return sum(prices)