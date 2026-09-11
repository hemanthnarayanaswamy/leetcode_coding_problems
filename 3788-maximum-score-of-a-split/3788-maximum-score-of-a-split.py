class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('-inf')

        suffixMin = [0]*n
        prefix = 0

        for i in range(n-1, -1, -1):
            if i < n-1:
                suffixMin[i] = min(suffixMin[i+1], nums[i+1])
            else:
                suffixMin[i] = nums[i]

        for i in range(n-1):
            prefix += nums[i]
            tmp = prefix - suffixMin[i]
            
            if tmp > res:
                res = tmp
        
        return res
        