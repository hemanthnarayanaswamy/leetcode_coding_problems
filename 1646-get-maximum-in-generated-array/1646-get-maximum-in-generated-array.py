class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        nums = [0, 1] + [0] * (n-1)

        for i in range(2, n+1):
            q, r = divmod(i, 2)
            nums[i] += nums[q]
            if r:
                nums[i] += nums[q+1]          

        return max(nums) 
        