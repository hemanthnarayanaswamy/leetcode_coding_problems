class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        res = []

        prefixSum = [0]*n
        suffixMin = [0]*n

        for i in range(n):
            if i > 0:
                prefixSum[i] = prefixSum[i-1] + nums[i]
            else:
                prefixSum[i] = nums[i]
        
        for i in range(n-1, -1, -1):
            if i < n-1:
                suffixMin[i] = min(suffixMin[i+1], nums[i+1])
            else:
                suffixMin[i] = nums[i]
        
        for p, s in zip(prefixSum, suffixMin[:-1]):
            res.append(p - s)
        
        return max(res)
        