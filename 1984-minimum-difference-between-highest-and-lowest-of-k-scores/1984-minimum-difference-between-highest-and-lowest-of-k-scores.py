class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        n = len(nums)

        for i in range(n-k+1):
            diff = nums[i+k-1] - nums[i]
            if diff < res:
                res = diff
        
        return res