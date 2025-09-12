class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre = [0]
        for i, c in enumerate(nums):
            pre.append(pre[-1] + c)
            
        ans = 0
        for i, c in enumerate(nums):
            start = max(0, i-c)
            ans += pre[i+1] - pre[start]
        
        return ans