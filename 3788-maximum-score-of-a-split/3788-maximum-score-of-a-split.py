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
                res.append(prefixSum[i] - suffixMin[i])
            else:
                suffixMin[i] = nums[i]
        
        return max(res)
        