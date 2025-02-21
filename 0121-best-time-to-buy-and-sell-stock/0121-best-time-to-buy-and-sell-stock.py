class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock_price = float('inf')
        max_profit = 0 

        for price in prices:
            min_stock_price = min(price, min_stock_price)
            max_profit = max(max_profit, price - min_stock_price)
        return max_profit