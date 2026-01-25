class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if k == 1 or n == 1:
            return 0 

        nums.sort()
        res = float('inf')
        
        for i in range(n-k+1):
            diff = nums[i+k-1] - nums[i]
            if diff < res:
                res = diff
        return res
        