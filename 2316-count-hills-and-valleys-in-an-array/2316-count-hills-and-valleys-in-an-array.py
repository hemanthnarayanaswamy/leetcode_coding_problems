class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        numsU = []
        ans = 0

        for i in range(len(nums)):
            if i == 0 or i == len(nums)-1:
                numsU.append(nums[i])
            elif nums[i] !=  nums[i-1]:
                numsU.append(nums[i])

        for i in range(1, len(numsU)-1):
            p, c, n = numsU[i-1], numsU[i], numsU[i+1]

            if c > p and c > n:
                ans += 1
            elif c < p and c < n:
                ans += 1
        
        return ans