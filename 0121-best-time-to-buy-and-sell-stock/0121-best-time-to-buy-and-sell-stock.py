class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stock_price = float("inf")
        max_profit = 0 

        for price in prices:
            if price < min_stock_price:
                min_stock_price = price
            
            profit = price - min_stock_price

            if profit > max_profit:
                max_profit = profit 
                
        return max_profit
        