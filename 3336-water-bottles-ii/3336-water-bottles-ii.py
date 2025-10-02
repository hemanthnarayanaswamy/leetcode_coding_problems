class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = emptyBottles = numBottles 

        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            numExchange += 1
            bottlesDrunk += 1
            emptyBottles += 1

        return bottlesDrunk
        