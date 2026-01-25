class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(k, len(nums)):
            diff = nums[i] - nums[i-k+1]
            if diff < res:
                res = diff
        
        return res