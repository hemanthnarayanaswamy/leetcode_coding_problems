class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        total = numBottles
        drunk = numBottles
        while total >= numExchange:
                total -= numExchange
                total += 1
                drunk += 1
                numExchange += 1
        return drunk