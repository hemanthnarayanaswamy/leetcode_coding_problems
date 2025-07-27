class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        numsU = []
        ans = 0

        for i in range(len(nums)):
            if numsU and numsU[-1] == nums[i]:
                continue
            numsU.append(nums[i])

        for i in range(1, len(numsU)-1):
            p, c, n = numsU[i-1], numsU[i], numsU[i+1]

            if p < c > n or p > c < n:
                ans += 1
        
        return ans