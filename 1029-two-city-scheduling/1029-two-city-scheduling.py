class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        a = b = len(costs) // 2
        sortedCosts = sorted(costs, key=lambda x: abs(x[0] - x[1]), reverse=True)
        totalCost = 0

        for costA, costB in sortedCosts:
            if a and costA < costB:
                totalCost += costA
                a -= 1
            elif b and costB < costA:
                totalCost += costB
                b -= 1
            elif not a and costA < costB:
                totalCost += costB
                b -= 1
            else:
                totalCost += costA
                a -= 1
        
        return totalCost
