class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock_price = prices[0]
        max_profit = 0 

        for price in prices:
            profit = price - min_stock_price

            if profit > max_profit:
                max_profit = profit

            if price < min_stock_price:
                min_stock_price = price

        return max_profit
        