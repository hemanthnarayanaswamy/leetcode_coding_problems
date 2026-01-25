class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums)-k+1):
            diff = nums[i+k-1] - nums[i]
            if diff < res:
                res = diff
        
        return res