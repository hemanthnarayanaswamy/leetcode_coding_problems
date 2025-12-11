class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1] + [0] * (n-1)

        for i in range(2, n+1):
            q, r = divmod(i, 2)

            if r == 0:
                nums[i] = nums[q]
            else:
                nums[i] = nums[q] + nums[q+1]

        return max(nums) 
        