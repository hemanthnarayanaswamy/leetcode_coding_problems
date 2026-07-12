class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9+7
        
        total = sum(nums)

        if total <= k:
            return 0
        
        n = ceil((total - k) / k)
        cost = (n * (n + 1)) // 2 

        return cost % MOD