class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        d = [0] * (n+1)

        for query in queries:
            l, r = query

            d[l] += -1
            d[r+1] += 1
        
        for i in range(1, n):
            d[i] += d[i-1]
        
        for i in range(n):
            if nums[i] + d[i] > 0:
                return False
        
        return True
