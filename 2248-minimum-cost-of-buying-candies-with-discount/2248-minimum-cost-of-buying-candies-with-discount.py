class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0

        for i in range(len(cost)):
            if (i+1) % 3 != 0:
                total += cost[i]
        
        return total
