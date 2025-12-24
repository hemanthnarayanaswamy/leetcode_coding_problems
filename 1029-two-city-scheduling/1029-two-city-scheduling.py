class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        sortedCosts = sorted(costs, key=lambda x: x[0] - x[1])  # Sort by cost difference (A - B)
        totalCost = 0

        for costA, costB in sortedCosts:
            if n:
                totalCost += costA
                n -= 1
            else:
                totalCost += costB

        return totalCost
