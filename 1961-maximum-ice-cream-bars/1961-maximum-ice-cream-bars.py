class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs) <= coins:
            return len(costs)
        
        bars = 0
        costs = sorted(costs)
        
        for cost in costs: 
            if coins - cost >= 0:
                bars += 1
                coins -= cost
        
        return bars

        