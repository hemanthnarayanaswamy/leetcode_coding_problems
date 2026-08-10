class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cost = 0
        
        if n > k:
            cost += k * (n - k)

        if m > k:
            cost +=  k * (m - k)
        
        return cost
                