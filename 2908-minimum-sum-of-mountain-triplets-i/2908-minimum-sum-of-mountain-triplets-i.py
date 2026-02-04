class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res = float('inf')
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                if nums[i] >= nums[j]:
                    break
                for k in range(j+1, n):
                    if nums[k] >= nums[j]:
                        continue
                    res = min(res, nums[i]+nums[j]+nums[k])
        
        return res if res != float('inf') else -1
