class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        bars = 0
        costs.sort()
        
        for cost in costs: 
            if cost <= coins:
                bars += 1
                coins -= cost
        
        return bars

        