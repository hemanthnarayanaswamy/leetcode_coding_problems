class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0

        for i in range(len(cost)):
            if i % 3 != 2: # Remember this logic We need to remove the every 3 element
                total += cost[i]
        
        return total