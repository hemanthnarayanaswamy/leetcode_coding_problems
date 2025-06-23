class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottlesDrink = emptyBottles = numBottles

        while emptyBottles >= numExchange:
            x, y = divmod(emptyBottles, numExchange)
            bottlesDrink += x
            emptyBottles = y + x
        
        return bottlesDrink