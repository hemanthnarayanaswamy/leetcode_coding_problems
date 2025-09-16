class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n = len(cost)
        res= [0] * n
        prefixMin = 100

        for i in range(n):
            res[i] = min(prefixMin, cost[i])
            prefixMin = res[i]
        
        return res